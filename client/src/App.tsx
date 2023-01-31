import { BrowserRouter, Route, Routes } from "react-router-dom";
import Routing from "./routing";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        {Routing.map((route) => {
          const Component = route.component;
          return (
            <Route
              caseSensitive
              path={route.path}
              key={route.path}
              element={<Component />}
            />
          );
        })}
      </Routes>
    </BrowserRouter>
  );
}

export default App;
