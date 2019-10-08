import React, { Component } from "react"
import styled from "styled-components"
import {
  Button,
  Modal,
  ModalHeader,
  ModalBody,
  ModalFooter,
  Form,
  FormGroup,
  Input,
  Label
} from "reactstrap"

const StyledForm = styled(Form)`
  max-width: 50%;
  text-align: center;
  margin: auto;
`

const Searchbar = () => {
  return (
    <StyledForm>
      <FormGroup>
        <Input type="text" name="card" id="cardSearch" placeholder="Search for a card..." />
      </FormGroup>
    </StyledForm>
  )
}

export default Searchbar
