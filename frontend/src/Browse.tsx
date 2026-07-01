import { useMemo, useState } from "react";
import type { CSSProperties } from "react";
import "./Browse.css";
import { Badge, Card, IconButton, Select, StatBar, Switch, Tag, TierBadge } from "./design-system";
import { TRACKS } from "./data/tracks";
import type { Track } from "./data/tracks";

const ENGINE_CLASSES = ["50cc", "100cc", "150cc", "200cc"];
const ALL_TRAITS = ["Shortcuts", "Anti-grav", "Glider", "Water", "Item-heavy", "Technical", "Chaos", "Beginner"];
const SORT_OPTIONS = [
  { value: "tier", label: "Tier (S → F)" },
  { value: "speed", label: "Speed" },
  { value: "technical", label: "Technical" },
  { value: "chaos", label: "Chaos" },
  { value: "shortcuts", label: "Shortcuts" },
];
const TIER_ORDER: Record<Track["tier"], number> = { S: 0, A: 1, B: 2, C: 3, D: 4, F: 5 };

const eyebrow: CSSProperties = {
  fontFamily: "var(--font-ui)",
  fontWeight: "var(--weight-semibold)",
  fontSize: "var(--text-xs)",
  letterSpacing: "var(--tracking-caps)",
  textTransform: "uppercase",
  color: "var(--ink-500)",
};

function statByLabel(track: Track, label: string) {
  return track.stats.find((s) => s.label.toLowerCase() === label)?.value ?? -1;
}

interface TrackCardProps {
  track: Track;
  favorited: boolean;
  onToggleFavorite: () => void;
}

function TrackCard({ track, favorited, onToggleFavorite }: TrackCardProps) {
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
        <TierBadge tier={track.tier} size="sm" style={{ position: "absolute", top: 12, left: 12 }} />
        <IconButton
          icon="heart"
          round
          size="sm"
          variant={favorited ? "primary" : "outline"}
          label={favorited ? "Remove favorite" : "Add favorite"}
          onClick={onToggleFavorite}
          style={{ position: "absolute", top: 10, right: 12 }}
        />
      </div>

      <div style={{ padding: 20, display: "flex", flexDirection: "column", gap: 14 }}>
        <div>
          <h3 style={{ fontFamily: "var(--font-display)", fontSize: "var(--text-xl)", color: "var(--ink-900)", margin: 0 }}>
            {track.name}
          </h3>
          <p style={{ fontFamily: "var(--font-body)", fontSize: "var(--text-sm)", color: "var(--ink-500)", margin: "4px 0 0" }}>
            {track.cup} &middot; {track.distanceKm} km &middot; {track.laps} laps
          </p>
        </div>

        <div className="mk-browse-traits">
          {track.traits.map((trait) => (
            <Badge key={trait} color="neutral" soft>
              {trait}
            </Badge>
          ))}
        </div>

        <div style={{ display: "flex", flexDirection: "column", gap: 10 }}>
          {track.stats.map((stat) => (
            <StatBar key={stat.label} label={stat.label} value={stat.value} color={stat.color} />
          ))}
        </div>
      </div>
    </Card>
  );
}

/**
 * Browse — search & filter every track in the catalog. Sidebar filters
 * (engine class, sort, traits, favorites) narrow the card grid on the right.
 */
export function Browse() {
  const [engineClass, setEngineClass] = useState("150cc");
  const [sortBy, setSortBy] = useState("tier");
  const [selectedTraits, setSelectedTraits] = useState<Set<string>>(new Set());
  const [favoritesOnly, setFavoritesOnly] = useState(false);
  const [favorites, setFavorites] = useState<Set<string>>(new Set());

  function toggleTrait(trait: string) {
    setSelectedTraits((prev) => {
      const next = new Set(prev);
      next.has(trait) ? next.delete(trait) : next.add(trait);
      return next;
    });
  }

  function toggleFavorite(id: string) {
    setFavorites((prev) => {
      const next = new Set(prev);
      next.has(id) ? next.delete(id) : next.add(id);
      return next;
    });
  }

  const tracks = useMemo(() => {
    const filtered = TRACKS.filter((t) => {
      if (favoritesOnly && !favorites.has(t.id)) return false;
      for (const trait of selectedTraits) if (!t.traits.includes(trait)) return false;
      return true;
    });
    return filtered.sort((a, b) =>
      sortBy === "tier" ? TIER_ORDER[a.tier] - TIER_ORDER[b.tier] : statByLabel(b, sortBy) - statByLabel(a, sortBy)
    );
  }, [selectedTraits, favoritesOnly, favorites, sortBy]);

  return (
    <div style={{ display: "flex", gap: 40, padding: 40, alignItems: "flex-start" }}>
      <aside style={{ width: 260, flexShrink: 0, display: "flex", flexDirection: "column", gap: 28 }}>
        <div style={{ display: "flex", flexDirection: "column", gap: 10 }}>
          <span style={eyebrow}>Engine class</span>
          <div style={{ display: "flex", flexWrap: "wrap", gap: 8 }}>
            {ENGINE_CLASSES.map((cc) => (
              <Tag key={cc} selected={engineClass === cc} onClick={() => setEngineClass(cc)}>
                {cc}
              </Tag>
            ))}
          </div>
        </div>

        <div style={{ display: "flex", flexDirection: "column", gap: 10 }}>
          <span style={eyebrow}>Sort by</span>
          <Select options={SORT_OPTIONS} value={sortBy} onChange={(e) => setSortBy(e.target.value)} />
        </div>

        <div style={{ display: "flex", flexDirection: "column", gap: 10 }}>
          <span style={eyebrow}>Track traits</span>
          <div style={{ display: "flex", flexWrap: "wrap", gap: 8 }}>
            {ALL_TRAITS.map((trait) => (
              <Tag key={trait} selected={selectedTraits.has(trait)} onClick={() => toggleTrait(trait)}>
                {trait}
              </Tag>
            ))}
          </div>
        </div>

        <div style={{ borderTop: "1px solid var(--border-subtle)", paddingTop: 20 }}>
          <Switch checked={favoritesOnly} onChange={setFavoritesOnly} label="Favorites only" />
        </div>
      </aside>

      <main style={{ flex: 1, minWidth: 0, display: "flex", flexDirection: "column", gap: 24 }}>
        <div style={{ display: "flex", alignItems: "baseline", justifyContent: "space-between" }}>
          <h1 style={{ fontFamily: "var(--font-display)", fontSize: "var(--text-3xl)", color: "var(--ink-900)", margin: 0 }}>
            All tracks
          </h1>
          <span style={{ fontFamily: "var(--font-mono)", fontSize: "var(--text-sm)", color: "var(--ink-500)" }}>
            {tracks.length} tracks &middot; {engineClass}
          </span>
        </div>

        <div className="mk-browse-grid">
          {tracks.map((track) => (
            <TrackCard
              key={track.id}
              track={track}
              favorited={favorites.has(track.id)}
              onToggleFavorite={() => toggleFavorite(track.id)}
            />
          ))}
        </div>
      </main>
    </div>
  );
}
