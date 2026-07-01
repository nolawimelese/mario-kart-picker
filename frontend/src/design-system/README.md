# MK Picker Design System — repo install

A drop-in folder for a **Vite + React + TypeScript** app. Components are real
`.tsx` (typed, extensionless imports, no stub files). Styling is plain CSS
custom properties — no runtime CSS-in-JS, no extra dependencies beyond `react`.

## 1. Copy this folder into your repo
Put it at e.g. `frontend/src/design-system/`. Structure:

```
design-system/
  index.ts            ← barrel: import everything from here
  styles.css          ← global entry (import ONCE)
  base.css
  tokens/             ← colors, typography, spacing, effects, fonts
  brand/   core/   forms/   navigation/   data/   feedback/   ← components
  assets/             ← source social glyphs (optional)
```

## 2. Load the styles once
In `src/main.tsx` (or your root entry):

```ts
import "./design-system/styles.css";
```

This pulls in the design tokens, base element styles, and the Google-Fonts
import (Lilita One, Fredoka, Nunito, Space Mono).

## 3. Use components
```tsx
import { Button, TierBadge, StatBar, Tabs } from "./design-system";

export function Example() {
  return (
    <div>
      <Button variant="primary" iconLeft="zap">Boost pick</Button>
      <TierBadge tier="S" />
      <StatBar label="Speed" value={82} color="var(--boost-500)" />
    </div>
  );
}
```

(With a path alias like `@/design-system`, import from there instead.)

## Notes
- **No build step needed** — Vite/esbuild transpiles the `.tsx` directly; nothing
  here imports anything but `react`.
- **Fonts load from Google Fonts CDN** via `tokens/fonts.css`. For
  production/offline, self-host: drop `.woff2` into `assets/fonts/` and replace
  the `@import` in `tokens/fonts.css` with `@font-face` rules.
- **Type strictness:** a couple of components attach CSS custom properties inside
  `style={{ ... }}` (e.g. `StatBar`'s segment overlay). Under `tsc --strict`
  these may need a cast; Vite's dev/build path (esbuild, no typecheck) runs them
  as-is.
- **Design tokens** are global CSS variables — use them anywhere
  (`var(--boost-500)`, `var(--font-display)`, `var(--shadow-pop)`,
  `var(--radius-lg)`). Full list in `tokens/`.

## Component inventory
Brand: `Logo`, `Icon` · Core: `Button`, `IconButton`, `Badge`, `Tag`,
`TierBadge`, `Card`, `Avatar` · Forms: `Input`, `Select`, `Checkbox`, `Switch` ·
Navigation: `Tabs` · Data: `StatBar` · Feedback: `Dialog`, `Toast`, `Tooltip`.
