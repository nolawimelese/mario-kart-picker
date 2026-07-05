import { useMemo, useState } from "react";
import type { CSSProperties } from "react";
import { useQuery } from "@tanstack/react-query";
import "./Browse.css";
import { Badge, Card, Input, Tag } from "./design-system";
import { fetchTracks } from "./api/tracks";
import type { Track } from "./api/tracks";

const ALL_TRAITS = [
  "Shortcuts",
  "Anti-grav",
  "Glider",
  "Water",
  "Item-heavy",
  "Technical",
  "Chaos",
  "Beginner",
];

const eyebrow: CSSProperties = {
  fontFamily: "var(--font-ui)",
  fontWeight: "var(--weight-semibold)",
  fontSize: "var(--text-xs)",
  letterSpacing: "var(--tracking-caps)",
  textTransform: "uppercase",
  color: "var(--ink-500)",
};

interface TrackCardProps {
  track: Track;
}

function TrackCard({ track }: TrackCardProps) {
  return (
    <Card pop interactive padding={0}>
      <div
        className="mk-track-card__header"
        style={{
          position: "relative",
          height: 110,
          background: track.headerColor,
          borderBottom: "var(--border-base) solid var(--ink-900)",
          borderTopLeftRadius: "calc(var(--radius-lg) - 2px)",
          borderTopRightRadius: "calc(var(--radius-lg) - 2px)",
        }}
      >
        {track.dlc && (
          <span
            title="DLC track"
            style={{
              position: "absolute",
              top: 12,
              left: 14,
              display: "flex",
              alignItems: "center",
              height: 26,
              padding: "0 9px",
              background: "var(--coin-500)",
              color: "var(--ink-900)",
              border: "2px solid var(--ink-900)",
              borderRadius: "var(--radius-pill)",
              boxShadow: "var(--shadow-pop-sm)",
              fontFamily: "var(--font-ui)",
              fontWeight: 700,
              fontSize: 10,
              letterSpacing: "0.04em",
            }}
          >
            DLC
          </span>
        )}
      </div>

      <div
        style={{
          padding: 20,
          display: "flex",
          flexDirection: "column",
          gap: 14,
        }}
      >
        <div>
          <h3
            style={{
              fontFamily: "var(--font-display)",
              fontSize: "var(--text-xl)",
              color: "var(--ink-900)",
              margin: 0,
            }}
          >
            {track.name}
          </h3>
          <p
            style={{
              fontFamily: "var(--font-body)",
              fontSize: "var(--text-sm)",
              color: "var(--ink-500)",
              margin: "4px 0 0",
            }}
          >
            {track.cup} &middot; {track.laps} laps
          </p>
        </div>

        <div className="mk-browse-traits">
          {track.traits.map((trait) => (
            <Badge key={trait} color="neutral" soft>
              {trait}
            </Badge>
          ))}
        </div>

        <p
          style={{
            fontFamily: "var(--font-body)",
            fontSize: "var(--text-sm)",
            color: "var(--ink-700)",
            margin: 0,
            lineHeight: 1.5,
          }}
        >
          {track.description}
        </p>
      </div>
    </Card>
  );
}

/**
 * Browse — search & filter every track in the catalog. Sidebar filters
 * (traits, favorites) narrow the card grid on the right.
 */
export function Browse() {
  const [search, setSearch] = useState("");
  const [selectedTraits, setSelectedTraits] = useState<Set<string>>(new Set());

  const {
    data,
    isPending,
    isError,
  } = useQuery({ queryKey: ["tracks"], queryFn: fetchTracks });

  function toggleTrait(trait: string) {
    setSelectedTraits((prev) => {
      const next = new Set(prev);
      next.has(trait) ? next.delete(trait) : next.add(trait);
      return next;
    });
  }

  const tracks = useMemo(() => {
    const query = search.trim().toLowerCase();
    return (data ?? []).filter((t) => {
      if (query && !t.name.toLowerCase().includes(query)) return false;
      for (const trait of selectedTraits)
        if (!t.traits.includes(trait)) return false;
      return true;
    });
  }, [data, search, selectedTraits]);

  return (
    <div
      style={{
        display: "flex",
        gap: 40,
        padding: 40,
        alignItems: "flex-start",
      }}
    >
      <aside
        style={{
          width: 260,
          flexShrink: 0,
          display: "flex",
          flexDirection: "column",
          gap: 28,
        }}
      >
        <Input
          icon="search"
          placeholder="Search tracks..."
          value={search}
          onChange={(e) => setSearch(e.target.value)}
        />

        <div style={{ display: "flex", flexDirection: "column", gap: 10 }}>
          <span style={eyebrow}>Track traits</span>
          <div style={{ display: "flex", flexWrap: "wrap", gap: 8 }}>
            {ALL_TRAITS.map((trait) => (
              <Tag
                key={trait}
                selected={selectedTraits.has(trait)}
                onClick={() => toggleTrait(trait)}
              >
                {trait}
              </Tag>
            ))}
          </div>
        </div>
      </aside>

      <main
        style={{
          flex: 1,
          minWidth: 0,
          display: "flex",
          flexDirection: "column",
          gap: 24,
        }}
      >
        <div
          style={{
            display: "flex",
            alignItems: "baseline",
            justifyContent: "space-between",
          }}
        >
          <h1
            style={{
              fontFamily: "var(--font-display)",
              fontSize: "var(--text-3xl)",
              color: "var(--ink-900)",
              margin: 0,
            }}
          >
            All tracks
          </h1>
          <span
            style={{
              fontFamily: "var(--font-mono)",
              fontSize: "var(--text-sm)",
              color: "var(--ink-500)",
            }}
          >
            {tracks.length} tracks
          </span>
        </div>

        {isPending ? (
          <p className="mk-browse-status">Loading tracks…</p>
        ) : isError ? (
          <p className="mk-browse-status">
            Couldn't reach the track server — is the backend running?
          </p>
        ) : (
          <div className="mk-browse-grid">
            {tracks.map((track) => (
              <TrackCard key={track.id} track={track} />
            ))}
          </div>
        )}
      </main>
    </div>
  );
}
