import { useMemo, useRef, useState } from "react";
import type { CSSProperties } from "react";
import { useMutation, useQuery } from "@tanstack/react-query";
import "./CoursePicker.css";
import { Badge, Button, Card, Icon, IconButton, Input } from "./design-system";
import { fetchTracks } from "./api/tracks";
import type { Track } from "./api/tracks";
import { fetchRecommendation } from "./api/recommend";
import type { Recommendation } from "./api/recommend";

/** Minimum time the "warming up the grid" animation stays up, for arcade feel. */
const MIN_SPIN_MS = 1400;
const FIELD_SIZE = 12;

/** Ordinal suffix helper — 1 → "1st", 11 → "11th", etc. */
function ordinal(n: number): string {
  const s = ["th", "st", "nd", "rd"];
  const v = n % 100;
  return n + (s[(v - 20) % 10] || s[v] || s[0]);
}

/** Backend score is ~0–1 (can dip below 0 / above 1); show a friendly 0–100. */
function pickScore(score: number): number {
  return Math.max(0, Math.min(100, Math.round(score * 100)));
}

const eyebrow: CSSProperties = {
  fontFamily: "var(--font-ui)",
  fontWeight: "var(--weight-semibold)",
  fontSize: "var(--text-xs)",
  letterSpacing: "var(--tracking-caps)",
  textTransform: "uppercase",
  color: "var(--boost-500)",
};

const stepNum: CSSProperties = {
  fontFamily: "var(--font-mono)",
  fontSize: "var(--text-sm)",
  fontWeight: 700,
  color: "var(--boost-500)",
};

const stepTitle: CSSProperties = {
  fontFamily: "var(--font-display)",
  fontSize: "var(--text-2xl)",
  color: "var(--ink-900)",
  margin: 0,
};

const stepHint: CSSProperties = {
  fontFamily: "var(--font-body)",
  fontSize: "var(--text-sm)",
  color: "var(--ink-500)",
  margin: "-8px 0 0",
};

const posStyleBase: CSSProperties = {
  display: "flex",
  alignItems: "center",
  justifyContent: "center",
  height: 62,
  borderRadius: "var(--radius-md)",
  border: "var(--border-base) solid var(--ink-900)",
  background: "var(--white)",
  boxShadow: "var(--shadow-pop-sm)",
  cursor: "pointer",
  transition:
    "transform 120ms var(--ease-snap), box-shadow 120ms var(--ease-snap), background 120ms",
};

const MEDAL: Record<number, string> = {
  1: "#f5c542",
  2: "#c9cdd4",
  3: "#cd7f42",
};

/** Floating decorative item-boxes behind the picker, echoing the mockup. */
interface Decor {
  r: string;
  top?: number;
  bottom?: number;
  left?: string;
  right?: string;
  size: number;
  bg: string;
  radius: string;
  dur: string;
  delay: string;
  opacity: number;
}
const DECOR: Decor[] = [
  {
    r: "-8deg",
    top: 70,
    left: "6%",
    size: 64,
    bg: "var(--star-purple)",
    radius: "var(--radius-lg)",
    dur: "5.2s",
    delay: "0s",
    opacity: 0.16,
  },
  {
    r: "6deg",
    top: 130,
    right: "8%",
    size: 52,
    bg: "var(--boo-cyan)",
    radius: "var(--radius-pill)",
    dur: "4.4s",
    delay: "0.4s",
    opacity: 0.16,
  },
  {
    r: "12deg",
    bottom: 110,
    left: "11%",
    size: 44,
    bg: "var(--coin-500)",
    radius: "var(--radius-md)",
    dur: "6s",
    delay: "0.9s",
    opacity: 0.18,
  },
  {
    r: "-14deg",
    bottom: 150,
    right: "12%",
    size: 58,
    bg: "var(--heart-pink)",
    radius: "var(--radius-pill)",
    dur: "5.6s",
    delay: "0.2s",
    opacity: 0.14,
  },
];

type Phase = "input" | "loading" | "result";

/**
 * Course Picker — the flagship. Tell us where you finished and which three
 * tracks are on the ballot, and we spin up the smartest one to vote for next
 * (scored by the real backend recommender).
 */
export function CoursePicker() {
  const [position, setPosition] = useState<number | null>(null);
  const [ballot, setBallot] = useState<Track[]>([]);
  const [search, setSearch] = useState("");
  const [phase, setPhase] = useState<Phase>("input");
  const [results, setResults] = useState<Recommendation[]>([]);
  const spinStart = useRef(0);
  const spinTimer = useRef<number | undefined>(undefined);

  const { data: allTracks } = useQuery({
    queryKey: ["tracks"],
    queryFn: fetchTracks,
  });

  const recommend = useMutation({
    mutationFn: () =>
      fetchRecommendation(
        position as number,
        ballot.map((t) => t.id),
      ),
    onMutate: () => {
      spinStart.current = Date.now();
      setPhase("loading");
    },
    onSuccess: (data) => {
      const wait = Math.max(0, MIN_SPIN_MS - (Date.now() - spinStart.current));
      spinTimer.current = window.setTimeout(() => {
        setResults(data);
        setPhase("result");
      }, wait);
    },
    onError: () => setPhase("input"),
  });

  const ballotFull = ballot.length >= 3;
  const canPick = position != null && ballot.length === 3;

  const searchResults = useMemo(() => {
    const q = search.trim().toLowerCase();
    if (!q) return [];
    const inBallot = new Set(ballot.map((t) => t.id));
    return (allTracks ?? []).filter(
      (t) => !inBallot.has(t.id) && t.name.toLowerCase().includes(q),
    );
  }, [allTracks, ballot, search]);

  function addTrack(track: Track) {
    if (ballotFull) return;
    setBallot((prev) => [...prev, track]);
    setSearch("");
  }
  function removeTrack(id: number) {
    setBallot((prev) => prev.filter((t) => t.id !== id));
  }
  function reset() {
    window.clearTimeout(spinTimer.current);
    recommend.reset();
    setPosition(null);
    setBallot([]);
    setSearch("");
    setResults([]);
    setPhase("input");
  }

  const ballotNames = ballot.map((t) => t.name).join(", ");
  const posLabel = position != null ? `${ordinal(position)}-place` : "";

  /* Join recommender results back to the ballot tracks for header color / meta. */
  const ranked = useMemo(
    () =>
      results
        .map((rec) => ({
          rec,
          track: ballot.find((t) => t.id === rec.trackId),
        }))
        .filter((r): r is { rec: Recommendation; track: Track } => !!r.track),
    [results, ballot],
  );
  const top = ranked[0];
  const runners = ranked.slice(1);

  return (
    <div
      style={{
        position: "relative",
        flex: 1,
        width: "100%",
        background: "var(--cream)",
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        padding: "48px 24px 72px",
        overflow: "hidden",
      }}
    >
      {/* Floating decor */}
      <div
        aria-hidden
        style={{
          position: "absolute",
          inset: 0,
          pointerEvents: "none",
          zIndex: 0,
        }}
      >
        {DECOR.map((d, i) => (
          <div
            key={i}
            className="mk-course-bob"
            style={
              {
                "--r": d.r,
                position: "absolute",
                top: d.top,
                bottom: d.bottom,
                left: d.left,
                right: d.right,
                width: d.size,
                height: d.size,
                borderRadius: d.radius,
                background: d.bg,
                border: "var(--border-base) solid var(--ink-900)",
                boxShadow: "var(--shadow-pop-sm)",
                opacity: d.opacity,
                animation: `mkbob ${d.dur} var(--ease-in-out) infinite ${d.delay}`,
              } as CSSProperties
            }
          />
        ))}
      </div>

      <div
        style={{
          position: "relative",
          zIndex: 1,
          width: "100%",
          maxWidth: 960,
          display: "flex",
          flexDirection: "column",
          gap: 28,
        }}
      >
        {/* Header */}
        <div
          style={{
            display: "flex",
            flexDirection: "column",
            gap: 8,
            textAlign: "center",
            alignItems: "center",
          }}
        >
          <span style={eyebrow}>Course Picker</span>
          <h1
            style={{
              fontFamily: "var(--font-display)",
              fontSize: "clamp(44px, 6vw, 68px)",
              color: "var(--ink-900)",
              margin: 0,
            }}
          >
            Pick your line.
          </h1>
          <p
            style={{
              fontFamily: "var(--font-body)",
              fontSize: "var(--text-lg)",
              color: "var(--text-body)",
              maxWidth: 520,
              margin: 0,
            }}
          >
            Tell us where you finished and what's on the ballot. We'll spin up
            the smartest track to vote for next.
          </p>
        </div>

        {recommend.isError && phase === "input" && (
          <div
            style={{
              display: "flex",
              alignItems: "center",
              gap: 10,
              padding: "12px 16px",
              background: "var(--shell-red)",
              color: "#fff",
              border: "var(--border-base) solid var(--ink-900)",
              borderRadius: "var(--radius-md)",
              boxShadow: "var(--shadow-pop-sm)",
            }}
          >
            <Icon name="alert" size={18} color="#fff" />
            <span
              style={{
                fontFamily: "var(--font-ui)",
                fontWeight: 600,
                fontSize: "var(--text-sm)",
              }}
            >
              Couldn't reach the recommender — is the backend running? Give it
              another spin.
            </span>
          </div>
        )}

        {/* ============ INPUT ============ */}
        {phase === "input" && (
          <Card pop padding={0}>
            <div
              style={{
                padding: 32,
                display: "flex",
                flexDirection: "column",
                gap: 34,
              }}
            >
              {/* Step 1 */}
              <div
                style={{ display: "flex", flexDirection: "column", gap: 16 }}
              >
                <div
                  style={{ display: "flex", alignItems: "baseline", gap: 12 }}
                >
                  <span style={stepNum}>01</span>
                  <h3 style={stepTitle}>Where'd you finish?</h3>
                </div>
                <p style={stepHint}>
                  Your last race — tap your finishing position.
                </p>
                <div
                  style={{
                    display: "grid",
                    gridTemplateColumns: "repeat(6, 1fr)",
                    gap: 12,
                  }}
                >
                  {Array.from({ length: FIELD_SIZE }, (_, i) => {
                    const n = i + 1;
                    const selected = position === n;
                    const isMedal = !!MEDAL[n];
                    const style: CSSProperties = selected
                      ? {
                          ...posStyleBase,
                          background: "var(--boost-500)",
                          boxShadow: "var(--shadow-pop)",
                          transform: "translate(-1px,-1px)",
                        }
                      : isMedal
                        ? { ...posStyleBase, background: MEDAL[n] }
                        : posStyleBase;
                    return (
                      <button
                        key={n}
                        type="button"
                        onClick={() => setPosition(n)}
                        style={style}
                      >
                        <span
                          style={{
                            fontFamily: "var(--font-display)",
                            fontSize: 24,
                            lineHeight: 1,
                            color: selected ? "#fff" : "var(--ink-900)",
                          }}
                        >
                          {n}
                        </span>
                      </button>
                    );
                  })}
                </div>
              </div>

              <div
                style={{
                  height: 2,
                  background: "var(--border-subtle)",
                  borderRadius: 2,
                }}
              />

              {/* Step 2 */}
              <div
                style={{ display: "flex", flexDirection: "column", gap: 16 }}
              >
                <div
                  style={{ display: "flex", alignItems: "baseline", gap: 12 }}
                >
                  <span style={stepNum}>02</span>
                  <h3 style={stepTitle}>What's on the ballot?</h3>
                  <span
                    style={{
                      marginLeft: "auto",
                      fontFamily: "var(--font-mono)",
                      fontSize: "var(--text-sm)",
                      color: "var(--ink-500)",
                    }}
                  >
                    {ballot.length}/3
                  </span>
                </div>
                <p style={stepHint}>
                  Search and add the 3 tracks Mario Kart is offering you.
                </p>

                <div style={{ position: "relative" }}>
                  <Input
                    icon="search"
                    placeholder="Search tracks…"
                    value={search}
                    onChange={(e) => setSearch(e.target.value)}
                    disabled={ballotFull}
                  />
                  {searchResults.length > 0 && (
                    <div
                      style={{
                        position: "absolute",
                        top: "calc(100% + 8px)",
                        left: 0,
                        right: 0,
                        zIndex: 20,
                        background: "var(--white)",
                        border: "var(--border-base) solid var(--ink-900)",
                        borderRadius: "var(--radius-md)",
                        boxShadow: "var(--shadow-pop)",
                        overflow: "hidden",
                        maxHeight: 280,
                        overflowY: "auto",
                      }}
                    >
                      {searchResults.map((t) => (
                        <button
                          key={t.id}
                          type="button"
                          onClick={() => addTrack(t)}
                          onMouseEnter={(e) =>
                            (e.currentTarget.style.background =
                              "var(--ink-100)")
                          }
                          onMouseLeave={(e) =>
                            (e.currentTarget.style.background = "transparent")
                          }
                          style={{
                            display: "flex",
                            width: "100%",
                            alignItems: "center",
                            gap: 12,
                            padding: "12px 16px",
                            background: "transparent",
                            border: "none",
                            borderBottom: "1px solid var(--border-subtle)",
                            cursor: "pointer",
                            textAlign: "left",
                          }}
                        >
                          <span
                            style={{
                              width: 14,
                              height: 34,
                              borderRadius: "var(--radius-xs)",
                              background: t.headerColor,
                              border: "var(--border-base) solid var(--ink-900)",
                              flexShrink: 0,
                            }}
                          />
                          <span
                            style={{
                              display: "flex",
                              flexDirection: "column",
                              gap: 2,
                              minWidth: 0,
                              flex: 1,
                            }}
                          >
                            <span
                              style={{
                                fontFamily: "var(--font-ui)",
                                fontWeight: 600,
                                fontSize: "var(--text-md)",
                                color: "var(--ink-900)",
                              }}
                            >
                              {t.name}
                            </span>
                            <span
                              style={{
                                fontFamily: "var(--font-body)",
                                fontSize: "var(--text-xs)",
                                color: "var(--ink-500)",
                              }}
                            >
                              {t.cup} · {t.laps} laps
                            </span>
                          </span>
                          <Icon
                            name="plus"
                            size={20}
                            color="var(--boost-500)"
                          />
                        </button>
                      ))}
                    </div>
                  )}
                </div>

                {/* Ballot slots */}
                <div
                  style={{
                    display: "grid",
                    gridTemplateColumns: "repeat(3, 1fr)",
                    gap: 12,
                  }}
                >
                  {[0, 1, 2].map((i) => {
                    const t = ballot[i];
                    if (t) {
                      return (
                        <div
                          key={t.id}
                          style={{
                            position: "relative",
                            display: "flex",
                            flexDirection: "column",
                            gap: 10,
                            padding: 14,
                            background: "var(--white)",
                            border: "var(--border-base) solid var(--ink-900)",
                            borderRadius: "var(--radius-md)",
                            boxShadow: "var(--shadow-pop-sm)",
                          }}
                        >
                          <span
                            style={{
                              height: 10,
                              borderRadius: "var(--radius-pill)",
                              background: t.headerColor,
                              border: "var(--border-base) solid var(--ink-900)",
                            }}
                          />
                          <span
                            style={{
                              fontFamily: "var(--font-ui)",
                              fontWeight: 600,
                              fontSize: "var(--text-md)",
                              color: "var(--ink-900)",
                              lineHeight: 1.15,
                            }}
                          >
                            {t.name}
                          </span>
                          <span
                            style={{
                              fontFamily: "var(--font-mono)",
                              fontSize: "var(--text-2xs)",
                              color: "var(--ink-500)",
                            }}
                          >
                            {t.cup}
                          </span>
                          <div
                            style={{ position: "absolute", top: 8, right: 8 }}
                          >
                            <IconButton
                              icon="x"
                              round
                              size="sm"
                              variant="outline"
                              label="Remove track"
                              onClick={() => removeTrack(t.id)}
                            />
                          </div>
                        </div>
                      );
                    }
                    return (
                      <div
                        key={`empty-${i}`}
                        style={{
                          display: "flex",
                          flexDirection: "column",
                          alignItems: "center",
                          justifyContent: "center",
                          gap: 6,
                          minHeight: 110,
                          border: "var(--border-base) dashed var(--ink-300)",
                          borderRadius: "var(--radius-md)",
                          background: "var(--ink-50)",
                        }}
                      >
                        <span
                          style={{
                            fontFamily: "var(--font-display)",
                            fontSize: "var(--text-xl)",
                            color: "var(--ink-300)",
                          }}
                        >
                          {i + 1}
                        </span>
                        <span
                          style={{
                            fontFamily: "var(--font-ui)",
                            fontSize: "var(--text-xs)",
                            color: "var(--ink-400)",
                            letterSpacing: "var(--tracking-caps)",
                            textTransform: "uppercase",
                          }}
                        >
                          Empty slot
                        </span>
                      </div>
                    );
                  })}
                </div>
              </div>

              {/* CTA */}
              <div
                style={{
                  display: "flex",
                  flexDirection: "column",
                  alignItems: "center",
                  gap: 12,
                  paddingTop: 4,
                }}
              >
                <Button
                  variant="primary"
                  size="lg"
                  iconRight="flag"
                  disabled={!canPick}
                  onClick={() => recommend.mutate()}
                >
                  Spin my pick
                </Button>
                {!canPick && (
                  <span
                    style={{
                      fontFamily: "var(--font-body)",
                      fontSize: "var(--text-sm)",
                      color: "var(--ink-400)",
                    }}
                  >
                    {position == null && ballot.length < 3
                      ? "Set your finishing position and add 3 tracks to spin."
                      : position == null
                        ? "Pick where you finished to spin."
                        : `Add ${3 - ballot.length} more track${3 - ballot.length === 1 ? "" : "s"} to spin.`}
                  </span>
                )}
              </div>
            </div>
          </Card>
        )}

        {/* ============ LOADING ============ */}
        {phase === "loading" && (
          <Card pop padding={0}>
            <div
              style={{
                padding: "44px 32px",
                display: "flex",
                flexDirection: "column",
                alignItems: "center",
                gap: 22,
              }}
            >
              <Icon
                name="dice"
                size={40}
                color="var(--boost-500)"
                className="mk-course-spin"
                style={{ animation: "mkspin 1.1s var(--ease-in-out) infinite" }}
              />
              <h2
                style={{
                  fontFamily: "var(--font-display)",
                  fontSize: "clamp(28px, 4vw, 40px)",
                  color: "var(--ink-900)",
                  textAlign: "center",
                  margin: 0,
                }}
              >
                Warming up the grid…
              </h2>
              <p
                style={{
                  fontFamily: "var(--font-body)",
                  fontSize: "var(--text-md)",
                  color: "var(--ink-500)",
                  textAlign: "center",
                  maxWidth: 460,
                  margin: 0,
                }}
              >
                Weighing {ballotNames} against your {posLabel} finish.
              </p>
              <div
                style={{
                  position: "relative",
                  width: "min(420px, 90%)",
                  height: 14,
                  borderRadius: "var(--radius-pill)",
                  background: "var(--ink-100)",
                  border: "var(--border-base) solid var(--ink-900)",
                  overflow: "hidden",
                }}
              >
                <div
                  className="mk-course-bar"
                  style={{
                    position: "absolute",
                    top: 0,
                    bottom: 0,
                    width: "40%",
                    borderRadius: "var(--radius-pill)",
                    background: "var(--boost-500)",
                    animation: "mkbar 1.1s var(--ease-in-out) infinite",
                  }}
                />
              </div>
              <div
                className="mk-course-checker"
                style={{
                  width: "100%",
                  height: 16,
                  borderRadius: "var(--radius-xs)",
                  animation: "mkchecker 0.9s linear infinite",
                  opacity: 0.5,
                }}
              />
            </div>
          </Card>
        )}

        {/* ============ RESULT ============ */}
        {phase === "result" && top && (
          <div
            className="mk-course-pop"
            style={{
              display: "flex",
              flexDirection: "column",
              gap: 20,
              animation: "mkpop 0.34s var(--ease-snap)",
            }}
          >
            {/* Recap */}
            <div
              style={{
                display: "flex",
                flexWrap: "wrap",
                alignItems: "center",
                gap: 10,
                justifyContent: "center",
              }}
            >
              <span
                style={{
                  fontFamily: "var(--font-ui)",
                  fontWeight: 600,
                  fontSize: "var(--text-sm)",
                  color: "var(--ink-500)",
                }}
              >
                You finished {ordinal(position as number)} · voting between{" "}
                {ballotNames}
              </span>
            </div>

            {/* Recommendation */}
            <Card pop padding={0}>
              <div
                style={{
                  position: "relative",
                  height: 96,
                  background: top.track.headerColor,
                  borderBottom: "var(--border-base) solid var(--ink-900)",
                  borderTopLeftRadius: "calc(var(--radius-lg) - 2px)",
                  borderTopRightRadius: "calc(var(--radius-lg) - 2px)",
                  display: "flex",
                  alignItems: "center",
                  padding: "0 24px",
                }}
              >
                <div
                  style={{
                    display: "inline-flex",
                    alignItems: "center",
                    gap: 8,
                    padding: "8px 14px",
                    background: "var(--ink-900)",
                    borderRadius: "var(--radius-pill)",
                  }}
                >
                  <span
                    style={{
                      width: 8,
                      height: 8,
                      borderRadius: "50%",
                      background: "var(--mushroom)",
                    }}
                  />
                  <span
                    style={{
                      fontFamily: "var(--font-ui)",
                      fontWeight: 700,
                      fontSize: "var(--text-xs)",
                      letterSpacing: "var(--tracking-caps)",
                      textTransform: "uppercase",
                      color: "var(--white)",
                    }}
                  >
                    Vote this track
                  </span>
                </div>
              </div>

              <div
                style={{
                  padding: 28,
                  display: "flex",
                  flexDirection: "column",
                  gap: 22,
                }}
              >
                <div
                  style={{ display: "flex", alignItems: "flex-start", gap: 18 }}
                >
                  <div style={{ flex: 1, minWidth: 0 }}>
                    <h2
                      style={{
                        fontFamily: "var(--font-display)",
                        fontSize: "var(--text-3xl)",
                        color: "var(--ink-900)",
                        lineHeight: 1.05,
                        margin: 0,
                      }}
                    >
                      {top.track.name}
                    </h2>
                    <p
                      style={{
                        fontFamily: "var(--font-body)",
                        fontSize: "var(--text-sm)",
                        color: "var(--ink-500)",
                        margin: "4px 0 0",
                      }}
                    >
                      {top.track.cup} · {top.track.laps} laps
                    </p>
                  </div>
                  <div style={{ textAlign: "right", flexShrink: 0 }}>
                    <div
                      style={{
                        fontFamily: "var(--font-mono)",
                        fontSize: "var(--text-4xl)",
                        fontWeight: 700,
                        color: "var(--ink-900)",
                        lineHeight: 1,
                      }}
                    >
                      {pickScore(top.rec.score)}
                    </div>
                    <div
                      style={{
                        fontFamily: "var(--font-ui)",
                        fontSize: "var(--text-2xs)",
                        letterSpacing: "var(--tracking-caps)",
                        textTransform: "uppercase",
                        color: "var(--ink-400)",
                      }}
                    >
                      Pick score
                    </div>
                  </div>
                </div>

                {top.track.traits.length > 0 && (
                  <div style={{ display: "flex", flexWrap: "wrap", gap: 8 }}>
                    {top.track.traits.map((tr) => (
                      <Badge key={tr} color="neutral" soft>
                        {tr}
                      </Badge>
                    ))}
                  </div>
                )}

                {/* Insight note */}
                <div
                  style={{
                    display: "flex",
                    gap: 12,
                    padding: "16px 18px",
                    background: "var(--boost-50)",
                    border: "var(--border-base) solid var(--ink-900)",
                    borderRadius: "var(--radius-md)",
                  }}
                >
                  <Icon
                    name="zap"
                    size={20}
                    color="var(--boost-500)"
                    style={{ flexShrink: 0, marginTop: 2 }}
                  />
                  <p
                    style={{
                      fontFamily: "var(--font-body)",
                      fontSize: "var(--text-md)",
                      color: "var(--ink-800)",
                      lineHeight: 1.5,
                      margin: 0,
                    }}
                  >
                    {top.rec.reason}
                  </p>
                </div>

                {/* Strategy + tips */}
                {top.rec.strategyName && (
                  <div
                    style={{
                      display: "flex",
                      flexDirection: "column",
                      gap: 10,
                    }}
                  >
                    <div
                      style={{ display: "flex", alignItems: "center", gap: 8 }}
                    >
                      <Icon name="route" size={18} color="var(--drift-500)" />
                      <span
                        style={{
                          fontFamily: "var(--font-display)",
                          fontSize: "var(--text-lg)",
                          color: "var(--ink-900)",
                        }}
                      >
                        {top.rec.strategyName}
                      </span>
                    </div>
                    <ul
                      style={{
                        display: "flex",
                        flexDirection: "column",
                        gap: 8,
                        margin: 0,
                        paddingLeft: 0,
                        listStyle: "none",
                      }}
                    >
                      {top.rec.strategyTips.map((tip, i) => (
                        <li
                          key={i}
                          style={{
                            display: "flex",
                            gap: 10,
                            alignItems: "flex-start",
                          }}
                        >
                          <Icon
                            name="check"
                            size={16}
                            color="var(--mushroom)"
                            style={{ flexShrink: 0, marginTop: 3 }}
                          />
                          <span
                            style={{
                              fontFamily: "var(--font-body)",
                              fontSize: "var(--text-sm)",
                              color: "var(--ink-700)",
                              lineHeight: 1.5,
                            }}
                          >
                            {tip}
                          </span>
                        </li>
                      ))}
                    </ul>
                  </div>
                )}
              </div>
            </Card>

            {/* Runners up */}
            {runners.length > 0 && (
              <div
                style={{ display: "flex", flexDirection: "column", gap: 12 }}
              >
                <span style={{ ...eyebrow, color: "var(--ink-500)" }}>
                  The other picks
                </span>
                {runners.map(({ rec, track }, i) => (
                  <div
                    key={rec.trackId}
                    style={{
                      display: "flex",
                      alignItems: "center",
                      gap: 16,
                      padding: "16px 18px",
                      background: "var(--white)",
                      border: "var(--border-base) solid var(--ink-900)",
                      borderRadius: "var(--radius-md)",
                      boxShadow: "var(--shadow-pop-sm)",
                    }}
                  >
                    <span
                      style={{
                        fontFamily: "var(--font-display)",
                        fontSize: "var(--text-xl)",
                        color: "var(--ink-300)",
                        width: 28,
                        textAlign: "center",
                        flexShrink: 0,
                      }}
                    >
                      #{i + 2}
                    </span>
                    <span
                      style={{
                        width: 14,
                        height: 40,
                        borderRadius: "var(--radius-xs)",
                        background: track.headerColor,
                        border: "var(--border-base) solid var(--ink-900)",
                        flexShrink: 0,
                      }}
                    />
                    <div style={{ flex: 1, minWidth: 0 }}>
                      <div
                        style={{
                          fontFamily: "var(--font-ui)",
                          fontWeight: 600,
                          fontSize: "var(--text-md)",
                          color: "var(--ink-900)",
                        }}
                      >
                        {track.name}
                      </div>
                      <div
                        style={{
                          fontFamily: "var(--font-body)",
                          fontSize: "var(--text-sm)",
                          color: "var(--ink-500)",
                        }}
                      >
                        {rec.reason}
                      </div>
                    </div>
                    <div style={{ textAlign: "right", flexShrink: 0 }}>
                      <span
                        style={{
                          fontFamily: "var(--font-mono)",
                          fontSize: "var(--text-xl)",
                          fontWeight: 700,
                          color: "var(--ink-600)",
                        }}
                      >
                        {pickScore(rec.score)}
                      </span>
                    </div>
                  </div>
                ))}
              </div>
            )}

            {/* Actions */}
            <div
              style={{
                display: "flex",
                flexWrap: "wrap",
                gap: 12,
                justifyContent: "center",
                paddingTop: 4,
              }}
            >
              <Button
                variant="outline"
                size="md"
                iconLeft="shuffle"
                onClick={() => recommend.mutate()}
              >
                Reroll the ballot
              </Button>
              <Button variant="ghost" size="md" onClick={reset}>
                Start over
              </Button>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}
