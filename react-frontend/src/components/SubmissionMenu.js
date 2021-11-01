import React from 'react';
import Button from '@material-ui/core/Button';
import Dialog from '@material-ui/core/Dialog';
import DialogActions from '@material-ui/core/DialogActions';
import DialogContent from '@material-ui/core/DialogContent';
import DialogContentText from '@material-ui/core/DialogContentText';
import DialogTitle from '@material-ui/core/DialogTitle';
import { NavLink } from 'react-router-dom';

export default function SubmissionMenu({}) {
  const [open, setOpen] = React.useState(false);

  const handleClickOpen = () => {
    setOpen(true);
  };

  const handleClose = () => {
    setOpen(false);
  };


  return (
    <div>
      <Button variant="outlined" color="primary" onClick={handleClickOpen}>
        Solve with Genetic Algorithm
      </Button>
      <Dialog
        open={open}
        onClose={handleClose}
        aria-labelledby="alert-dialog-title"
        aria-describedby="alert-dialog-description"
      >
        <DialogTitle id="alert-dialog-title">{"Continue to genetic algorithm?"}</DialogTitle>
        <DialogContent>
          <DialogContentText id="alert-dialog-description">
            Your current city configuration will be saved and you will be redirected to the genetic
            algorithm configuration menu.
          </DialogContentText>
        </DialogContent>
        <DialogActions>
          <Button onClick={handleClose} color="primary">
            Cancel
          </Button>
          <NavLink to='/solve' exact>
            <Button onClick={handleClose} color="primary" autoFocus>
                Continue
            </Button>
          </NavLink>
        </DialogActions>
      </Dialog>
    </div>
  );
}
