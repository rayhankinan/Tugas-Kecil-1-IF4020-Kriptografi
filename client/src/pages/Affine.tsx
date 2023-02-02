import React from "react";
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
      <UploadDisplayText
        displayText={displayText}
        setDisplayText={setDisplayText}
      />
      <UploadFileButton fileInput={fileInput} setFileInput={setFileInput} />
    </PageLayout>
  );
};

export default Affine;
