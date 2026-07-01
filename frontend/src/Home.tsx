import { useState } from "react";
import { TopNav } from "./design-system";
import { Browse } from "./Browse";

/**
 * MK Picker home page — TopNav plus the active section's content.
 * Course Picker and Kart Preview are still placeholders; Browse is live.
 */
export function Home() {
  const [tab, setTab] = useState("course-picker");

  return (
    <div
      style={{
        minHeight: "100vh",
        width: "100%",
        background: "var(--cream)",
        display: "flex",
        flexDirection: "column",
      }}
    >
      <TopNav value={tab} onChange={setTab} />
      {tab === "browse" ? (
        <Browse />
      ) : (
        <main
          style={{
            flex: 1,
            display: "flex",
            flexDirection: "column",
            alignItems: "center",
            justifyContent: "center",
            gap: 12,
            padding: 40,
          }}
        >
          <h1 style={{ fontSize: "clamp(40px, 6vw, 64px)", color: "var(--ink-900)", textAlign: "center" }}>
            Welcome to the grid.
          </h1>
          <p style={{ fontSize: "var(--text-lg)", color: "var(--text-muted)", textAlign: "center" }}>
            Pick a section above to get started.
          </p>
        </main>
      )}
    </div>
  );
}
