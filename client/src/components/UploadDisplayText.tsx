import React from "react";
import { Box, TextField } from "@mui/material";

interface UploadDisplayTextProps {
  displayText: string | undefined;
  setDisplayText: React.Dispatch<React.SetStateAction<string | undefined>>;
  placeholder: string;
}

const UploadDisplayText: React.FC<UploadDisplayTextProps> = ({
  displayText,
  setDisplayText,
  placeholder,
}: UploadDisplayTextProps) => {
  const handleChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    const { value } = event.target;

    setDisplayText(value);
  };

  return (
    <Box component="form" sx={{ flexGrow: 1 }} noValidate autoComplete="off">
      <TextField
        multiline
        fullWidth
        placeholder={placeholder}
        rows={25}
        variant="standard"
        value={displayText}
        onChange={handleChange}
      />
    </Box>
  );
};

export default UploadDisplayText;
