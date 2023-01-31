import React from "react";

const AffinePage: React.LazyExoticComponent<any> = React.lazy(() =>
  import("./pages/Affine").then((module) => ({
    default: module.default,
  }))
);

const AutoKeyVigenerePage: React.LazyExoticComponent<any> = React.lazy(() =>
  import("./pages/AutoKeyVigenere").then((module) => ({
    default: module.default,
  }))
);

const EnigmaPage: React.LazyExoticComponent<any> = React.lazy(() =>
  import("./pages/Enigma").then((module) => ({
    default: module.default,
  }))
);

const ExtendedVigenerePage: React.LazyExoticComponent<any> = React.lazy(() =>
  import("./pages/ExtendedVigenere").then((module) => ({
    default: module.default,
  }))
);

const HillPage: React.LazyExoticComponent<any> = React.lazy(() =>
  import("./pages/Hill").then((module) => ({
    default: module.default,
  }))
);

const Playfair: React.LazyExoticComponent<any> = React.lazy(() =>
  import("./pages/Playfair").then((module) => ({
    default: module.default,
  }))
);

const VigenerePage: React.LazyExoticComponent<any> = React.lazy(() =>
  import("./pages/Vigenere").then((module) => ({
    default: module.default,
  }))
);

const ErrorPage: React.LazyExoticComponent<any> = React.lazy(() =>
  import("./pages/Error").then((module) => ({
    default: module.default,
  }))
);

interface PageRouting {
  path: string;
  component: React.LazyExoticComponent<any>;
}

const Routing: PageRouting[] = [
  {
    path: "/affine",
    component: AffinePage,
  },
  {
    path: "/auto-key-vigenere",
    component: AutoKeyVigenerePage,
  },
  {
    path: "enigma",
    component: EnigmaPage,
  },
  {
    path: "/extended-vigenere",
    component: ExtendedVigenerePage,
  },
  {
    path: "/hill",
    component: HillPage,
  },
  {
    path: "/playfair",
    component: Playfair,
  },
  {
    path: "/vigenere",
    component: VigenerePage,
  },
  {
    path: "*",
    component: ErrorPage,
  },
];

export default Routing;
