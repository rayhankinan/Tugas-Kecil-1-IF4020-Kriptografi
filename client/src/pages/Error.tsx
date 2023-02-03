import React from "react";
import { Button, Stack } from "@mui/material";
import { useNavigate } from "react-router-dom";
import PageLayout from "@layout/PageLayout";

const Affine: React.FC = () => {
  const navigate = useNavigate();

  return (
    <PageLayout>
      <Stack direction="column" spacing={2}>
        <Button onClick={() => navigate(-1)}>Go Back</Button>
      </Stack>
    </PageLayout>
  );
};

export default Affine;
