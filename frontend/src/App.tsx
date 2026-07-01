import { useState } from "react";
import "./App.css";
import { Splash } from "./Splash";
import { Home } from "./Home";

function App() {
  const [view, setView] = useState<"splash" | "home">("splash");

  return view === "splash" ? (
    <Splash onStart={() => setView("home")} />
  ) : (
    <Home />
  );
}

export default App;
