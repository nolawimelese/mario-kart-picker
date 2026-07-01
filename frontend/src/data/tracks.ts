import type { IconName } from "../design-system";

export type Tier = "S" | "A" | "B" | "C" | "D" | "F";

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
  tier: Tier;
  distanceKm: number;
  laps: number;
  /** Traits shown as chips under the title (also used for filtering). */
  traits: string[];
  /** CSS color value for the checkered header banner. */
  headerColor: string;
  stats: TrackStat[];
}

/**
 * Mock track catalog for the Browse page. The backend `/tracks` endpoint
 * only stores name + strategies today, so this stands in until cup/tier/
 * stat fields are seeded — swap for a fetch() once the API grows them.
 */
export const TRACKS: Track[] = [
  {
    id: "sunset-speedway",
    name: "Sunset Speedway",
    cup: "Boost Cup",
    tier: "S",
    distanceKm: 2.1,
    laps: 3,
    traits: ["Shortcuts", "Anti-grav"],
    headerColor: "var(--boost-500)",
    stats: [
      { label: "Speed", value: 88, color: "var(--boost-500)" },
      { label: "Shortcuts", value: 76, color: "var(--boost-500)" },
      { label: "Recovery", value: 70, color: "var(--boost-500)" },
    ],
  },
  {
    id: "neon-circuit",
    name: "Neon Circuit",
    cup: "Star Cup",
    tier: "S",
    distanceKm: 2.4,
    laps: 3,
    traits: ["Technical", "Anti-grav"],
    headerColor: "var(--star-purple)",
    stats: [
      { label: "Technical", value: 90, color: "var(--star-purple)" },
      { label: "Speed", value: 80, color: "var(--star-purple)" },
      { label: "Shortcuts", value: 58, color: "var(--star-purple)" },
    ],
  },
  {
    id: "skyline-rush",
    name: "Skyline Rush",
    cup: "Star Cup",
    tier: "S",
    distanceKm: 2.6,
    laps: 3,
    traits: ["Glider", "Technical"],
    headerColor: "var(--drift-500)",
    stats: [
      { label: "Speed", value: 92, color: "var(--drift-500)" },
      { label: "Technical", value: 85, color: "var(--drift-500)" },
      { label: "Shortcuts", value: 62, color: "var(--drift-500)" },
    ],
  },
  {
    id: "coral-cove",
    name: "Coral Cove",
    cup: "Shell Cup",
    tier: "A",
    distanceKm: 1.9,
    laps: 3,
    traits: ["Water", "Item-heavy"],
    headerColor: "var(--boo-cyan)",
    stats: [
      { label: "Item luck", value: 82, color: "var(--boo-cyan)" },
      { label: "Chaos", value: 78, color: "var(--boo-cyan)" },
      { label: "Speed", value: 64, color: "var(--boo-cyan)" },
    ],
  },
  {
    id: "volcano-vault",
    name: "Volcano Vault",
    cup: "Star Cup",
    tier: "A",
    distanceKm: 2.3,
    laps: 3,
    traits: ["Chaos", "Anti-grav"],
    headerColor: "var(--shell-red)",
    stats: [
      { label: "Chaos", value: 88, color: "var(--shell-red)" },
      { label: "Speed", value: 76, color: "var(--shell-red)" },
      { label: "Item luck", value: 72, color: "var(--shell-red)" },
    ],
  },
  {
    id: "galaxy-gate",
    name: "Galaxy Gate",
    cup: "Boost Cup",
    tier: "A",
    distanceKm: 2.8,
    laps: 3,
    traits: ["Anti-grav", "Chaos"],
    headerColor: "var(--star-purple)",
    stats: [
      { label: "Speed", value: 84, color: "var(--star-purple)" },
      { label: "Technical", value: 78, color: "var(--star-purple)" },
      { label: "Chaos", value: 76, color: "var(--star-purple)" },
    ],
  },
  {
    id: "turbo-twist-bayou",
    name: "Turbo Twist Bayou",
    cup: "Shell Cup",
    tier: "B",
    distanceKm: 2.0,
    laps: 3,
    traits: ["Glider", "Beginner"],
    headerColor: "var(--mushroom)",
    stats: [
      { label: "Speed", value: 70, color: "var(--mushroom)" },
      { label: "Recovery", value: 65, color: "var(--mushroom)" },
      { label: "Item luck", value: 60, color: "var(--mushroom)" },
    ],
  },
  {
    id: "dune-drift-raceway",
    name: "Dune Drift Raceway",
    cup: "Lightning Cup",
    tier: "B",
    distanceKm: 2.2,
    laps: 3,
    traits: ["Technical", "Shortcuts"],
    headerColor: "var(--coin-500)",
    stats: [
      { label: "Technical", value: 68, color: "var(--coin-600)" },
      { label: "Speed", value: 72, color: "var(--coin-600)" },
      { label: "Shortcuts", value: 55, color: "var(--coin-600)" },
    ],
  },
  {
    id: "frostbite-falls",
    name: "Frostbite Falls",
    cup: "Ice Cup",
    tier: "B",
    distanceKm: 2.1,
    laps: 3,
    traits: ["Water", "Glider"],
    headerColor: "var(--boo-cyan)",
    stats: [
      { label: "Speed", value: 66, color: "var(--boo-cyan)" },
      { label: "Item luck", value: 74, color: "var(--boo-cyan)" },
      { label: "Chaos", value: 58, color: "var(--boo-cyan)" },
    ],
  },
  {
    id: "rickety-rope-bridge",
    name: "Rickety Rope Bridge",
    cup: "Shell Cup",
    tier: "C",
    distanceKm: 1.7,
    laps: 3,
    traits: ["Beginner"],
    headerColor: "var(--drift-400)",
    stats: [
      { label: "Speed", value: 55, color: "var(--drift-400)" },
      { label: "Recovery", value: 80, color: "var(--drift-400)" },
      { label: "Shortcuts", value: 40, color: "var(--drift-400)" },
    ],
  },
  {
    id: "boulder-canyon-byway",
    name: "Boulder Canyon Byway",
    cup: "Lightning Cup",
    tier: "D",
    distanceKm: 2.5,
    laps: 3,
    traits: ["Chaos", "Item-heavy"],
    headerColor: "var(--ink-500)",
    stats: [
      { label: "Speed", value: 50, color: "var(--ink-500)" },
      { label: "Chaos", value: 62, color: "var(--ink-500)" },
      { label: "Item luck", value: 68, color: "var(--ink-500)" },
    ],
  },
  {
    id: "foggy-swamp-speedway",
    name: "Foggy Swamp Speedway",
    cup: "Shell Cup",
    tier: "F",
    distanceKm: 1.8,
    laps: 3,
    traits: ["Beginner", "Water"],
    headerColor: "var(--ink-400)",
    stats: [
      { label: "Speed", value: 40, color: "var(--ink-400)" },
      { label: "Recovery", value: 45, color: "var(--ink-400)" },
      { label: "Item luck", value: 50, color: "var(--ink-400)" },
    ],
  },
];
