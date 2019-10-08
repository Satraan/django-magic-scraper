import React, { Component } from "react"
import Modal from "./components/Modal"
import Searchbar from "./components/Searchbar"
import { ApolloProvider } from "react-apollo"
import { ApolloClient, HttpLink, InMemoryCache } from "apollo-boost"
const todoItems = [
  {
    id: 1,
    title: "Go to Market",
    description: "Buy ingredients to prepare dinner",
    completed: true
  },
  {
    id: 2,
    title: "Study",
    description: "Read Algebra and History textbook for upcoming test",
    completed: false
  },
  {
    id: 3,
    title: "Sally's books",
    description: "Go to library to rent sally's books",
    completed: true
  },
  {
    id: 4,
    title: "Article",
    description: "Write article on how to use django with react",
    completed: false
  }
]
class App extends Component {
  constructor(props) {
    super(props)
    this.state = {
      modal: false,
      viewCompleted: false,
      activeItem: {
        title: "",
        description: "",
        completed: false
      },
      todoList: todoItems
    }
  }

  render() {
    const httpLink = new HttpLink({ uri: "http://localhost:8000/graphql" })

    const client = new ApolloClient({
      link: httpLink,
      cache: new InMemoryCache(),
      fetchOptions: {
        mode: "no-cors"
      }
    })

    return (
      <ApolloProvider client={client}>
        <main className="content">
          <h1 className="text-white text-uppercase text-center my-4">Mox Monolith</h1>
          {/* <Searchbar /> */}
        </main>
      </ApolloProvider>
    )
  }
}
export default App
