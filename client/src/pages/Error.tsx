import React from "react";
import { Button } from "@mui/material";
import { useNavigate } from "react-router-dom";
import PageLayout from "@layout/PageLayout";

const Affine: React.FC = () => {
  const navigate = useNavigate();

  return (
    <PageLayout>
      <Button onClick={() => navigate(-1)}>Go Back</Button>
    </PageLayout>
  );
};

export default Affine;
