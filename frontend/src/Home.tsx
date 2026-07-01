import { TopNav } from "./design-system";

/**
 * MK Picker home page — TopNav plus a placeholder content area.
 * Real track/tier-list/strategy views will replace this section.
 */
export function Home() {
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
      <TopNav />
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
    </div>
  );
}
