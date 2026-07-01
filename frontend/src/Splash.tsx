import "./Splash.css";
import { Logo, Button } from "./design-system";

export interface SplashProps {
  /** Called when the user clicks "Let's Race". */
  onStart?: () => void;
}

/**
 * MK Picker startup / splash screen.
 * Full-viewport cream frame with the arcade checker motif, floating item-box
 * shapes, the wordmark, and the "Let's Race" entry CTA.
 */
export function Splash({ onStart }: SplashProps) {
  return (
    <div
      style={{
        minHeight: "100vh",
        width: "100%",
        background: "var(--cream)",
        overflow: "hidden",
        position: "relative",
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        justifyContent: "center",
        fontFamily: "var(--font-body)",
      }}
    >
      {/* top + bottom checker strips */}
      <div className="mk-splash-checker mk-splash-checker--top" />
      <div className="mk-splash-checker mk-splash-checker--bottom" />

      {/* floating accent shapes */}
      <div
        className="mk-splash-shape"
        style={{
          top: "15%",
          left: "11%",
          width: 34,
          height: 34,
          borderRadius: 999,
          background: "var(--drift-500)",
          animation: "mkBob 4.5s ease-in-out infinite",
        }}
      />
      <div
        className="mk-splash-shape"
        style={{
          top: "24%",
          right: "12%",
          width: 52,
          height: 52,
          borderRadius: 14,
          background: "var(--coin-500)",
          animation: "mkBob2 5.2s ease-in-out infinite",
        }}
      />
      <div
        className="mk-splash-shape"
        style={{
          bottom: "20%",
          left: "15%",
          width: 26,
          height: 26,
          borderRadius: 999,
          background: "var(--shell-red)",
          animation: "mkBob2 6s ease-in-out infinite",
        }}
      />
      <div
        className="mk-splash-shape"
        style={{
          bottom: "23%",
          right: "16%",
          width: 40,
          height: 40,
          borderRadius: 12,
          background: "var(--mushroom)",
          animation: "mkBob 5.6s ease-in-out infinite",
        }}
      />

      {/* center content */}
      <div
        style={{
          display: "flex",
          flexDirection: "column",
          alignItems: "center",
          gap: 24,
          zIndex: 2,
          padding: 40,
          animation: "mkFloatIn 0.6s var(--ease-out) both",
        }}
      >
        <div
          className="mk-eyebrow"
          style={{ fontSize: 14, letterSpacing: "0.14em" }}
        >
          Starting grid · Ready to roll
        </div>

        <Logo variant="full" size={76} />

        <h1
          style={{
            fontSize: "clamp(56px, 9vw, 104px)",
            color: "var(--ink-900)",
            textAlign: "center",
            lineHeight: 0.98,
            marginTop: 4,
          }}
        >
          Pick your line.
        </h1>

        <p
          style={{
            fontSize: "var(--text-lg)",
            color: "var(--text-muted)",
            textAlign: "center",
            maxWidth: 580,
          }}
        >
          Your co-pilot for choosing the perfect track. Filter by traits,
          compare stats, build tier lists — or let us spin you a pick.
        </p>

        {/* loading bar */}
        <div
          style={{
            display: "flex",
            flexDirection: "column",
            alignItems: "center",
            gap: 10,
            marginTop: 6,
          }}
        >
          <div
            style={{
              width: 400,
              maxWidth: "80vw",
              height: 14,
              background: "var(--ink-100)",
              border: "2px solid var(--ink-900)",
              borderRadius: 999,
              overflow: "hidden",
              position: "relative",
            }}
          >
            <div className="mk-splash-bar" />
          </div>
          <span
            style={{
              fontFamily: "var(--font-mono)",
              fontSize: 12,
              color: "var(--ink-500)",
              letterSpacing: "0.04em",
            }}
          >
            WARMING UP THE GRID…
          </span>
        </div>

        <div style={{ marginTop: 14 }}>
          <Button
            variant="primary"
            size="lg"
            iconRight="flag"
            onClick={onStart}
          >
            Let's Race
          </Button>
        </div>
      </div>
    </div>
  );
}
