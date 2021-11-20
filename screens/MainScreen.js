import React from 'react';
import { StyleSheet, View, Text, TouchableHighlight } from 'react-native';
import Header from './todo_header'
import Body from './todo_body'

class MainScreen extends React.Component {
  state = {
    todos: []
  }

  addTodo = (todo) => {
    const newTodo = {
      id: Date.now(),
      text: todo,
      completed: false,
    }
    this.setState(prevState => ({
      todos: [
        newTodo,
        ...prevState.todos
      ]
    }));
    console.log(this.state.todos);
  }

  checkTodo = (id) => {
    this.setState(prevState => {
      const [ todo ] = prevState.todos.filter(e => e.id === id);
      todo.completed = !todo.completed;
      return ({
        todos: [
            ...prevState.todos
        ]
      })
    });
  }

  removeTodo = (id) => {
    this.setState(prevState => {
      const index = prevState.todos.findIndex(e => e.id === id);
      prevState.todos.splice(index, 1);
      return ({
        todos: [
            ...prevState.todos
        ]
      })
    });
  }

  toChellenge = async () => {
    this.props.navigation.navigate("Challenge", {})
  }

  toSearch = async () => {
    this.props.navigation.navigate("Search", {})
  }

  render() {
    return (
      <>
      <View style={styles.container}>
        <TouchableHighlight onPress={this.toSearch}>
          <View style = {styles.btn1}>
            <Text style={styles.btntext}>Search</Text>
          </View>
        </TouchableHighlight>
        <TouchableHighlight onPress={this.toChellenge}>
          <View style = {styles.btn}>
            <Text style={styles.btntext}>Chellenge</Text>
          </View>
        </TouchableHighlight>
      </View>
      <View style = {styles.container1}>
        <Header addTodo={this.addTodo}/>
        <Body todos={this.state.todos} checkTodo = {this.checkTodo} removeTodo = {this.removeTodo}/>
      </View>
      </>
    );
  }
}

const styles = StyleSheet.create({
  container: {
    flexDirection: 'row',
    paddingTop: 10,
    backgroundColor: "#EEE",
  },
  container1: {
    flex: 1,
    flexDirection: 'column',
    paddingTop: 0,
    backgroundColor: "#EEE",
  },
  title: {
    fontWeight: "800",
    fontSize: 30, 
    marginLeft: 20,
    marginBottom: 20,
  },

  btn : {
    width: 100,
    height: 48,
    backgroundColor: "#ffffff",
    borderRadius: 8,
    borderColor: "#D0D0D0",
    borderWidth: 1,
    borderStyle: "solid",
    alignItems: "center",
    alignSelf: "flex-end",
    justifyContent: "center",
    lineHeight: 48,
    marginTop: 0,
    marginRight: 20,
    marginLeft: 180,
    shadowColor: "#333333",
    shadowOffset: {
      width: 0,
      height: 0.5,
    },
    shadowOpacity: 0.2,
    shadowRadius: 1.41,
    elevation: 2,
  },

  btn1 : {
    width: 100,
    height: 48,
    backgroundColor: "#ffffff",
    borderRadius: 8,
    borderColor: "#D0D0D0",
    borderWidth: 1,
    borderStyle: "solid",
    alignItems: "center",
    alignSelf: "flex-start",
    justifyContent: "center",
    lineHeight: 48,
    marginTop: 0,
    marginLeft: 20,
    shadowColor: "#333333",
    shadowOffset: {
      width: 0,
      height: 0.5,
    },
    shadowOpacity: 0.2,
    shadowRadius: 1.41,
    elevation: 2,
  },

  btntext : {
    fontSize: 16,
    fontWeight: "bold",
    color: "#AFAFAF",
    textShadowColor: "rgba(0, 0, 0, 0.1)",
    textShadowOffset: { width: -0.5, height: 0.5 },
    textShadowRadius: 10,
  },
});

export default MainScreen;