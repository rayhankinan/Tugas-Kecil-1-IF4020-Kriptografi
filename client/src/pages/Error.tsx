import React from "react";
import { Button, Stack, Typography } from "@mui/material";
import { useNavigate } from "react-router-dom";
import PageLayout from "@layout/PageLayout";

const Error: React.FC = () => {
  const navigate = useNavigate();

  return (
    <PageLayout>
      <Stack direction="column" spacing={2}>
        <center>
          <Typography variant="h1" component="h2">
            Page Not Found!
          </Typography>
        </center>
        <Button onClick={() => navigate(-1)}>Go Back</Button>
      </Stack>
    </PageLayout>
  );
};

export default Error;
