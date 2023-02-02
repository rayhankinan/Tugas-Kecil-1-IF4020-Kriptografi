import React from "react";
import { FormControlLabel, Switch } from "@mui/material";

interface SwitchDisplayViewProps {
  isSeparated: boolean;
  setIsSeparated: React.Dispatch<React.SetStateAction<boolean>>;
}

const SwitchDisplayView: React.FC<SwitchDisplayViewProps> = ({
  isSeparated,
  setIsSeparated,
}: SwitchDisplayViewProps) => {
  const handleChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    const { checked } = event.target;

    setIsSeparated(checked);
  };

  return (
    <FormControlLabel
      control={<Switch checked={isSeparated} onChange={handleChange} />}
      label={isSeparated ? "Separated" : "Default"}
    />
  );
};

export default SwitchDisplayView;
