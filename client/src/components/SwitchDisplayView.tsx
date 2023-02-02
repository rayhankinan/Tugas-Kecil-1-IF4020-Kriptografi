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
  const [checked, setChecked] = React.useState<boolean>(false);

  const handleChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    const { checked } = event.target;

    setChecked(checked);
  };

  return (
    <FormControlLabel
      control={<Switch checked={checked} onChange={handleChange} />}
      label={checked ? "Separated" : "Default"}
    />
  );
};

export default SwitchDisplayView;
