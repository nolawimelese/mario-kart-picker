import type { IconName } from "../design-system";

export interface TrackStat {
  label: string;
  value: number;
  color: string;
  icon?: IconName;
}

export interface Track {
  id: string;
  name: string;
  cup: string;
  distanceKm: number;
  laps: number;
  /** Traits shown as chips under the title (also used for filtering). */
  traits: string[];
  /** CSS color value for the checkered header banner. */
  headerColor: string;
  stats: TrackStat[];
  /** Short flavor blurb shown on the track card. */
  description: string;
}

/**
 * Mock track catalog for the Browse page. The backend `/tracks` endpoint
 * only stores name + strategies today, so this stands in until cup/
 * stat fields are seeded — swap for a fetch() once the API grows them.
 */
export const TRACKS: Track[] = [
  {
    id: "sunset-speedway",
    name: "Sunset Speedway",
    cup: "Boost Cup",
    distanceKm: 2.1,
    laps: 3,
    traits: ["Shortcuts", "Anti-grav"],
    headerColor: "var(--boost-500)",
    stats: [
      { label: "Speed", value: 88, color: "var(--boost-500)" },
      { label: "Shortcuts", value: 76, color: "var(--boost-500)" },
      { label: "Recovery", value: 70, color: "var(--boost-500)" },
    ],
    description:
      "A sun-drenched coastal loop where boost pads chain into gravity-flipped overpasses — hold your line and the whole track rewards you with speed.",
  },
  {
    id: "neon-circuit",
    name: "Neon Circuit",
    cup: "Star Cup",
    distanceKm: 2.4,
    laps: 3,
    traits: ["Technical", "Anti-grav"],
    headerColor: "var(--star-purple)",
    stats: [
      { label: "Technical", value: 90, color: "var(--star-purple)" },
      { label: "Speed", value: 80, color: "var(--star-purple)" },
      { label: "Shortcuts", value: 58, color: "var(--star-purple)" },
    ],
    description:
      "Neon signage and mirrored skyscrapers frame a tight, banked circuit built for drift chains — miss an apex here and you'll feel it.",
  },
  {
    id: "skyline-rush",
    name: "Skyline Rush",
    cup: "Star Cup",
    distanceKm: 2.6,
    laps: 3,
    traits: ["Glider", "Technical"],
    headerColor: "var(--drift-500)",
    stats: [
      { label: "Speed", value: 92, color: "var(--drift-500)" },
      { label: "Technical", value: 85, color: "var(--drift-500)" },
      { label: "Shortcuts", value: 62, color: "var(--drift-500)" },
    ],
    description:
      "Gliders launch you between rooftop gardens high above the clouds, with wind gusts that punish sloppy air control on the way down.",
  },
  {
    id: "coral-cove",
    name: "Coral Cove",
    cup: "Shell Cup",
    distanceKm: 1.9,
    laps: 3,
    traits: ["Water", "Item-heavy"],
    headerColor: "var(--boo-cyan)",
    stats: [
      { label: "Item luck", value: 82, color: "var(--boo-cyan)" },
      { label: "Chaos", value: 78, color: "var(--boo-cyan)" },
      { label: "Speed", value: 64, color: "var(--boo-cyan)" },
    ],
    description:
      "A lagoon dotted with item boxes bobbing on lily pads — pure chaos when the pack bunches up at the underwater tunnel entrance.",
  },
  {
    id: "volcano-vault",
    name: "Volcano Vault",
    cup: "Star Cup",
    distanceKm: 2.3,
    laps: 3,
    traits: ["Chaos", "Anti-grav"],
    headerColor: "var(--shell-red)",
    stats: [
      { label: "Chaos", value: 88, color: "var(--shell-red)" },
      { label: "Speed", value: 76, color: "var(--shell-red)" },
      { label: "Item luck", value: 72, color: "var(--shell-red)" },
    ],
    description:
      "Molten rivers carve through a cracked-open mountain, collapsing bridges forcing last-second anti-grav detours through the lava flow.",
  },
  {
    id: "galaxy-gate",
    name: "Galaxy Gate",
    cup: "Boost Cup",
    distanceKm: 2.8,
    laps: 3,
    traits: ["Anti-grav", "Chaos"],
    headerColor: "var(--star-purple)",
    stats: [
      { label: "Speed", value: 84, color: "var(--star-purple)" },
      { label: "Technical", value: 78, color: "var(--star-purple)" },
      { label: "Chaos", value: 76, color: "var(--star-purple)" },
    ],
    description:
      "A zero-gravity ribbon of track spiraling through an asteroid field, where a single well-timed boost can send you looping past the whole pack.",
  },
  {
    id: "turbo-twist-bayou",
    name: "Turbo Twist Bayou",
    cup: "Shell Cup",
    distanceKm: 2.0,
    laps: 3,
    traits: ["Glider", "Beginner"],
    headerColor: "var(--mushroom)",
    stats: [
      { label: "Speed", value: 70, color: "var(--mushroom)" },
      { label: "Recovery", value: 65, color: "var(--mushroom)" },
      { label: "Item luck", value: 60, color: "var(--mushroom)" },
    ],
    description:
      "A lazy, sun-baked bayou run with wide turns and forgiving guardrails — a friendly first track for karts still learning to drift.",
  },
  {
    id: "dune-drift-raceway",
    name: "Dune Drift Raceway",
    cup: "Lightning Cup",
    distanceKm: 2.2,
    laps: 3,
    traits: ["Technical", "Shortcuts"],
    headerColor: "var(--coin-500)",
    stats: [
      { label: "Technical", value: 68, color: "var(--coin-600)" },
      { label: "Speed", value: 72, color: "var(--coin-600)" },
      { label: "Shortcuts", value: 55, color: "var(--coin-600)" },
    ],
    description:
      "Sand dunes shift after every lap, opening and burying alternate paths through this desert raceway — no two laps play out the same.",
  },
  {
    id: "frostbite-falls",
    name: "Frostbite Falls",
    cup: "Ice Cup",
    distanceKm: 2.1,
    laps: 3,
    traits: ["Water", "Glider"],
    headerColor: "var(--boo-cyan)",
    stats: [
      { label: "Speed", value: 66, color: "var(--boo-cyan)" },
      { label: "Item luck", value: 74, color: "var(--boo-cyan)" },
      { label: "Chaos", value: 58, color: "var(--boo-cyan)" },
    ],
    description:
      "Icy switchbacks wind behind a roaring waterfall frozen mid-plunge, with patches of black ice that keep even careful drivers honest.",
  },
  {
    id: "rickety-rope-bridge",
    name: "Rickety Rope Bridge",
    cup: "Shell Cup",
    distanceKm: 1.7,
    laps: 3,
    traits: ["Beginner"],
    headerColor: "var(--drift-400)",
    stats: [
      { label: "Speed", value: 55, color: "var(--drift-400)" },
      { label: "Recovery", value: 80, color: "var(--drift-400)" },
      { label: "Shortcuts", value: 40, color: "var(--drift-400)" },
    ],
    description:
      "A creaky wooden bridge sways over a bottomless canyon — slow and nerve-wracking, but forgiving enough that a fall rarely costs the race.",
  },
  {
    id: "boulder-canyon-byway",
    name: "Boulder Canyon Byway",
    cup: "Lightning Cup",
    distanceKm: 2.5,
    laps: 3,
    traits: ["Chaos", "Item-heavy"],
    headerColor: "var(--ink-500)",
    stats: [
      { label: "Speed", value: 50, color: "var(--ink-500)" },
      { label: "Chaos", value: 62, color: "var(--ink-500)" },
      { label: "Item luck", value: 68, color: "var(--ink-500)" },
    ],
    description:
      "A rockslide-prone canyon road where boulders tumble across the racing line without warning — expect the unexpected on every straight.",
  },
  {
    id: "foggy-swamp-speedway",
    name: "Foggy Swamp Speedway",
    cup: "Shell Cup",
    distanceKm: 1.8,
    laps: 3,
    traits: ["Beginner", "Water"],
    headerColor: "var(--ink-400)",
    stats: [
      { label: "Speed", value: 40, color: "var(--ink-400)" },
      { label: "Recovery", value: 45, color: "var(--ink-400)" },
      { label: "Item luck", value: 50, color: "var(--ink-400)" },
    ],
    description:
      "Thick fog rolls low over still swamp water, hiding the next turn until you're nearly on top of it — a slow, moody starter track.",
  },
];
