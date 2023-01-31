import React, { LazyExoticComponent } from "react";

interface PageRouting {
  path: string;
  component: LazyExoticComponent<any>;
}

const Routing: PageRouting[] = [];

export default Routing;
