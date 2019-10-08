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
import Downshift from "downshift"

const StyledSelect = styled.div`
  max-width: 50%;
  text-align: center;
  margin: auto;
`
const items = [
  { value: "apple" },
  { value: "pear" },
  { value: "orange" },
  { value: "grape" },
  { value: "banana" }
]

const Searchbar = () => {
  return (
    <Downshift
      onChange={selection =>
        alert(selection ? `You selected ${selection.value}` : "Selection Cleared")
      }
      itemToString={item => (item ? item.value : "")}
    >
      {({
        getInputProps,
        getItemProps,
        getLabelProps,
        getMenuProps,
        isOpen,
        inputValue,
        highlightedIndex,
        selectedItem
      }) => (
        <div>
          <StyledSelect>
            <label {...getLabelProps()}>Enter a fruit</label>
            <input {...getInputProps()} />
            <ul {...getMenuProps()}>
              {isOpen
                ? items
                    .filter(item => !inputValue || item.value.includes(inputValue))
                    .map((item, index) => (
                      <li
                        {...getItemProps({
                          key: item.value,
                          index,
                          item,
                          style: {
                            backgroundColor: highlightedIndex === index ? "lightgray" : "white",
                            fontWeight: selectedItem === item ? "bold" : "normal"
                          }
                        })}
                      >
                        {item.value}
                      </li>
                    ))
                : null}
            </ul>
          </StyledSelect>
        </div>
      )}
    </Downshift>
  )
}

export default Searchbar
