import React from "react";
import { Button } from "@mui/material";
import { Clear as ClearIcon } from "@mui/icons-material";

interface ClearFileButtonProps {
  fileInput: File | undefined;
  setFileInput: React.Dispatch<React.SetStateAction<File | undefined>>;
}

const ClearFileButton: React.FC<ClearFileButtonProps> = ({
  fileInput,
  setFileInput,
}) => {
  const handleClear = () => {
    setFileInput(undefined);
  };

  return (
    <Button
      variant="contained"
      component="label"
      startIcon={<ClearIcon />}
      disabled={fileInput === undefined}
      onClick={handleClear}
    >
      Clear
    </Button>
  );
};

export default ClearFileButton;
