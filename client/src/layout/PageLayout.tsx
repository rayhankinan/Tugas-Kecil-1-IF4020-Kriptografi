import React from "react";
import { Container } from "@mui/material";
import NavigationBar from "@components/NavigationBar";

interface PageLayoutProps {
  children?: JSX.Element | JSX.Element[] | string | string[];
}

type PageLayoutComponent = ({}: PageLayoutProps) => JSX.Element;

const PageLayout: PageLayoutComponent = (props: PageLayoutProps) => {
  return (
    <React.Fragment>
      <NavigationBar />
      <Container maxWidth="lg">{props.children}</Container>
    </React.Fragment>
  );
};

export default PageLayout;
