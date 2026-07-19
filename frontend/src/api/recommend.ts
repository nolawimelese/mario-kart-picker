const API_URL = import.meta.env.VITE_API_URL ?? "/api";

/** One ranked track from the recommender, best-first. */
export interface Recommendation {
  trackId: number;
  name: string;
  /** Recommender score, normalized to [0, 1]. */
  score: number;
  /** Short, actionable tips tied to the best-fit strategy (empty if the track has none). */
  strategyTips: string[];
  /** Human-readable explanation of why this track scored where it did. */
  reason: string;
  /** True only for the top pick. */
  recommended: boolean;
}

/**
 * Ask the backend which of the ballot tracks to vote for, given where you
 * finished. Returns the tracks sorted best-first.
 */
export async function fetchRecommendation(
  position: number,
  trackIds: number[],
): Promise<Recommendation[]> {
  const res = await fetch(`${API_URL}/recommend`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ position, trackIds }),
  });
  if (!res.ok) throw new Error(`Failed to fetch recommendation: ${res.status}`);
  return res.json();
}
