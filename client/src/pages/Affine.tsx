import React from "react";
import { Container, Stack } from "@mui/material";
import PageLayout from "@layout/PageLayout";
import useDeepCompareEffect from "@hooks/deep-compare-effect";
import UploadDisplayText from "@components/UploadDisplayText";
import UploadFileButton from "@components/UploadFileButton";

const Affine: React.FC = () => {
  const [displayText, setDisplayText] = React.useState<string>();
  const [fileInput, setFileInput] = React.useState<File>();

  useDeepCompareEffect(() => {
    if (!fileInput) return;

    const reader = new FileReader();
    reader.onload = (evt) => {
      if (!evt.target) return;
      setDisplayText(evt.target.result as string);
    };

    reader.readAsText(fileInput);
  }, [fileInput]);

  return (
    <PageLayout>
      <Stack direction="row" spacing={2}>
        <Container maxWidth="lg">
          <UploadDisplayText
            displayText={displayText}
            setDisplayText={setDisplayText}
          />
          <UploadFileButton fileInput={fileInput} setFileInput={setFileInput} />
        </Container>
        <Container maxWidth="lg">{/* Output */}</Container>
      </Stack>
    </PageLayout>
  );
};

export default Affine;
