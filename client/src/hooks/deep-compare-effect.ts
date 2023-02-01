import React from "react";
import _ from "lodash";

const deepCompareEquals = (value: any, other: any) => {
  return _.isEqual(value, other);
};

const useDeepCompareMemoize = (value: any) => {
  const ref = React.useRef();

  if (!deepCompareEquals(value, ref.current)) {
    ref.current = value;
  }

  return ref.current;
};

const useDeepCompareEffect = (
  callback: React.EffectCallback,
  dependencies: React.DependencyList
) => {
  React.useEffect(callback, dependencies.map(useDeepCompareMemoize));
};

export default useDeepCompareEffect;
