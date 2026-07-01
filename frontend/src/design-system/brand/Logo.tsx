import React from "react";

export interface LogoProps extends React.HTMLAttributes<HTMLSpanElement> {
  /** Base size in px (drives the whole lockup). Default 32. */
  size?: number;
  /** "full" = badge + wordmark, "mark" = just the MK badge. Default "full". */
  variant?: "full" | "mark";
  /** Set true on dark backgrounds to flip the wordmark to white. */
  onDark?: boolean;
}

/**
 * MK Picker wordmark / lockup.
 * Type-based logo (Lilita One) — a chunky "MK" badge with a checkered-flag
 * accent next to the PICKER wordmark. No external image needed.
 */
export function Logo({ size = 32, variant = "full", onDark = false, style, ...rest }: LogoProps) {
  const ink = onDark ? "var(--white)" : "var(--ink-900)";
  const badge = (
    <span
      style={{
        display: "inline-grid",
        placeItems: "center",
        width: size * 1.18,
        height: size * 1.18,
        borderRadius: size * 0.32,
        background: "var(--boost-500)",
        color: "#fff",
        fontFamily: "var(--font-display)",
        fontSize: size * 0.62,
        lineHeight: 1,
        letterSpacing: "-0.04em",
        border: `${Math.max(2, size * 0.08)}px solid var(--ink-900)`,
        boxShadow: `${Math.max(2, size * 0.09)}px ${Math.max(2, size * 0.09)}px 0 var(--ink-900)`,
        paddingTop: size * 0.04,
        flexShrink: 0,
      }}
    >
      MK
    </span>
  );

  if (variant === "mark") {
    return <span style={{ display: "inline-flex", ...style }} {...rest}>{badge}</span>;
  }

  return (
    <span
      style={{ display: "inline-flex", alignItems: "center", gap: size * 0.34, ...style }}
      {...rest}
    >
      {badge}
      <span
        style={{
          fontFamily: "var(--font-display)",
          fontSize: size * 0.86,
          lineHeight: 1,
          letterSpacing: "-0.01em",
          color: ink,
          display: "inline-flex",
          alignItems: "center",
          gap: size * 0.22,
          paddingTop: size * 0.06,
        }}
      >
        Picker
        <span
          aria-hidden="true"
          style={{
            width: size * 0.5,
            height: size * 0.5,
            borderRadius: size * 0.14,
            backgroundImage:
              "conic-gradient(var(--ink-900) 90deg, transparent 90deg 180deg, var(--ink-900) 180deg 270deg, transparent 270deg)",
            backgroundColor: onDark ? "var(--white)" : "var(--coin-500)",
            backgroundSize: `${size * 0.25}px ${size * 0.25}px`,
          }}
        />
      </span>
    </span>
  );
}
