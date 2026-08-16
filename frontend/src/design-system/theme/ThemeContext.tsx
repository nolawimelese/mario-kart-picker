import React, { createContext, useContext, useEffect, useState } from "react";

export type Theme = "light" | "dark";
/** What the user asked for: a fixed theme, or "system" to follow the OS. */
export type ThemePreference = Theme | "system";

interface ThemeContextValue {
  /** The resolved theme — what's actually on screen. */
  darkMode: boolean;
  /** What the user picked; "system" while the theme follows the OS. */
  preference: ThemePreference;
  setPreference: (next: ThemePreference) => void;
}

const ThemeContext = createContext<ThemeContextValue | null>(null);

const STORAGE_KEY = "mkpicker:theme";

const DARK_QUERY = "(prefers-color-scheme: dark)";

/** Reads the saved preference, or null if the user has never picked one (or storage is unavailable). */
function readStoredPreference(): ThemePreference | null {
  try {
    const stored = localStorage.getItem(STORAGE_KEY);
    return stored === "dark" || stored === "light" || stored === "system" ? stored : null;
  } catch {
    return null;
  }
}

/** Storage can throw in private-browsing modes — the theme still applies for this session. */
function storePreference(preference: ThemePreference) {
  try {
    localStorage.setItem(STORAGE_KEY, preference);
  } catch {
    /* preference just won't persist */
  }
}

/** The OS-level preference; light if the browser can't tell us. */
function readSystemTheme(): Theme {
  return window.matchMedia?.(DARK_QUERY).matches ? "dark" : "light";
}

/** Applies the active theme to <html data-theme> so tokens/colors.css can react to it. */
export function ThemeProvider({ children }: { children: React.ReactNode }) {
  // Never picked one before → follow the system, same as the old implicit behaviour.
  const [preference, setPreferenceState] = useState<ThemePreference>(() => readStoredPreference() ?? "system");
  const [systemTheme, setSystemTheme] = useState<Theme>(readSystemTheme);

  const theme: Theme = preference === "system" ? systemTheme : preference;

  useEffect(() => {
    if (theme === "dark") {
      document.documentElement.dataset.theme = "dark";
    } else {
      delete document.documentElement.dataset.theme;
    }
  }, [theme]);

  // Track the OS preference live; it only reaches the page while preference is "system".
  useEffect(() => {
    const media = window.matchMedia?.(DARK_QUERY);
    if (!media) return;
    const onChange = (e: MediaQueryListEvent) => setSystemTheme(e.matches ? "dark" : "light");
    media.addEventListener("change", onChange);
    return () => media.removeEventListener("change", onChange);
  }, []);

  const value: ThemeContextValue = {
    darkMode: theme === "dark",
    preference,
    setPreference: (next) => {
      setPreferenceState(next);
      storePreference(next);
    },
  };

  return <ThemeContext.Provider value={value}>{children}</ThemeContext.Provider>;
}

// eslint-disable-next-line react-refresh/only-export-components -- hook is colocated with its provider
export function useTheme(): ThemeContextValue {
  const ctx = useContext(ThemeContext);
  if (!ctx) throw new Error("useTheme must be used within a ThemeProvider");
  return ctx;
}
