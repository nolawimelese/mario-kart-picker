export interface Track {
  id: number;
  name: string;
  cup: string;
  laps: number;
  /** Traits shown as chips under the title (also used for filtering). */
  traits: string[];
  /** Slippery off-road classification: "None" or a Light/Medium/Heavy
   * Sand/Ice grade (from MK8DX in-game statistics). */
  terrain: string;
  /** CSS color value for the checkered header banner. */
  headerColor: string;
  /** Short flavor blurb shown on the track card. */
  description: string;
  /** True for DLC (Booster Course Pass) tracks — shows a DLC pill on the card. */
  dlc: boolean;
}

const API_URL = import.meta.env.VITE_API_URL ?? "/api";

export async function fetchTracks(): Promise<Track[]> {
  const res = await fetch(`${API_URL}/tracks`);
  if (!res.ok) throw new Error(`Failed to fetch tracks: ${res.status}`);
  return res.json();
}
