import React from "react";

export interface CardProps extends React.HTMLAttributes<HTMLDivElement> {
  /** Chunky arcade outline + hard offset shadow. */
  pop?: boolean;
  /** Lift on hover (for clickable cards). */
  interactive?: boolean;
  /** Inner padding in px. Default 20. */
  padding?: number;
}

/**
 * Card — the base surface. Default is a soft-elevated rounded card; set
 * `pop` for the chunky arcade outline + hard offset shadow.
 */
export function Card({ children, pop = false, interactive = false, padding = 20, style, ...rest }: CardProps) {
  const base = {
    background: "var(--surface-card)",
    borderRadius: "var(--radius-lg)",
    padding,
    border: pop ? "var(--border-base) solid var(--ink-900)" : "var(--border-thin) solid var(--border-subtle)",
    boxShadow: pop ? "var(--shadow-pop)" : "var(--shadow-sm)",
    transition: "transform var(--dur-base) var(--ease-snap), box-shadow var(--dur-base) var(--ease-snap)",
    ...style,
  };
  return (
    <div
      onMouseEnter={interactive ? (e) => {
        e.currentTarget.style.transform = "translate(-2px,-2px)";
        e.currentTarget.style.boxShadow = pop ? "var(--shadow-pop-lg)" : "var(--shadow-md)";
      } : undefined}
      onMouseLeave={interactive ? (e) => {
        e.currentTarget.style.transform = "";
        e.currentTarget.style.boxShadow = pop ? "var(--shadow-pop)" : "var(--shadow-sm)";
      } : undefined}
      style={{ ...base, cursor: interactive ? "pointer" : "default" }}
      {...rest}
    >
      {children}
    </div>
  );
}
