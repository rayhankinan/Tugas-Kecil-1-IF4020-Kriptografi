import React from "react";
import {
  AppBar,
  Box,
  Drawer,
  Toolbar,
  Typography,
  IconButton,
} from "@mui/material";
import { Menu as MenuIcon } from "@mui/icons-material";

const NavigationBar: React.FC = () => {
  const [drawerOpened, setDrawerOpened] = React.useState(false);

  const toggleDrawer = () => {
    setDrawerOpened(!drawerOpened);
  };

  return (
    <Box sx={{ flexGrow: 1 }}>
      <AppBar position="static">
        <Toolbar>
          <IconButton
            size="large"
            edge="start"
            color="inherit"
            aria-label="menu"
            sx={{ mr: 2 }}
            onClick={toggleDrawer}
          >
            <MenuIcon />
          </IconButton>
          <Typography variant="h6" component="div" sx={{ flexGrow: 1 }}>
            Tugas Kecil 1 IF4020 Kriptografi
          </Typography>
          <Drawer anchor="left" open={drawerOpened} onClose={toggleDrawer}>
            {/* TODO: Navigation List */}
          </Drawer>
        </Toolbar>
      </AppBar>
    </Box>
  );
};

export default NavigationBar;
