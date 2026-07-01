import "./App.css";
import { Splash } from "./Splash";

function App() {
  return <Splash onStart={() => console.log("start")} />;
}

export default App;
