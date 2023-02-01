import React from "react";
import { Box, TextField } from "@mui/material";

interface UploadDisplayTextProps {
  displayText: string | undefined;
  setDisplayText: React.Dispatch<React.SetStateAction<string | undefined>>;
}

const UploadDisplayText: React.FC<UploadDisplayTextProps> = (
  props: UploadDisplayTextProps
) => {
  const handleChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    const { value } = event.target;
    props.setDisplayText(value);
  };

  return (
    <Box component="form" sx={{ flexGrow: 1 }} noValidate autoComplete="off">
      <TextField
        label="Text Input"
        multiline
        fullWidth
        rows={10}
        defaultValue={props.displayText}
        variant="standard"
        onChange={handleChange}
      />
    </Box>
  );
};

export default UploadDisplayText;
