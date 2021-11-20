import axios from 'axios';
import React, {Component} from 'react';
import { TouchableHighlight } from 'react-native';
import { ImageBackground } from 'react-native';
import {View, Text, StyleSheet, TextInput} from 'react-native';

class LogIn extends Component {
  state = {
    ID: '',
    Password: '',
  };

  onIDInput = event => {
    this.setState({
      ID: event,
    });
  };

  onPWInput = event => {
    this.setState({
      Password: event,
    });
  };
  
  _signIn = async () => {
    try {
      const response = await axios.get(
        ''
      );
      
      this.props.navigation.navigate("MainScreen", {ID: this.state.ID, PW : this.state.Password})
    } catch(e) {

    }
  }

  _signUp = async () => {
    this.props.navigation.navigate("SignUp", {ID: this.state.ID, PW : this.state.Password})
  }
  
  render() {
    return (
      <View style={styles.container}>
        <ImageBackground
          source={require("../assets/background.png")}
          resizeMode="cover"
          style={styles.backgroundimage}
        >
          <Text style={styles.text1}>ID</Text>
          <TextInput value={this.state.ID} style={styles.input} onChangeText={this.onIDInput}/>
          <Text style={styles.text1}>Password</Text>
          <TextInput value={this.state.Password} style={styles.input} onChangeText={this.onPWInput}/>
          <TouchableHighlight onPress = {this._signIn}>
            <View style = {styles.btn}>
              <Text style = {styles.btnText}>SignIn</Text>
            </View>
          </TouchableHighlight>
          <TouchableHighlight onPress = {this._signUp}>
            <View style = {styles.btn}>
              <Text style = {styles.btnText}>SignUp</Text>
            </View>
          </TouchableHighlight>
        </ImageBackground>
      </View>
    );
  }
}

const styles = StyleSheet.create({
  //나중에 여기 스타일 바꾸기
  input: {
    width: '90%',
    backgroundColor: 'white',
    marginTop: 20,
    marginLeft : 20,
    fontSize: 25,
    padding: 10,
  },

  container: {
    flex: 1,
    alignItems: "center",
    width: "100%",
    height: 600,
    flexDirection: "column",
  },

  text1: {
    textAlign: "center",
    fontWeight: "bold",
    fontSize: 20,
    marginBottom: 12,
    marginTop: 30,
    marginLeft : 20,
    marginRight: 20,
    textShadowColor: "rgba(0, 0, 0, 0.1)",
    textShadowOffset: { width: -0.5, height: 0.5 },
    textShadowRadius: 10,
  },

  backgroundimage: {
    width: "100%",
    height: "100%",
  },

  btn: {
    width: 340,
    height: 48,
    backgroundColor: "#ffffff",
    borderRadius: 8,
    borderColor: "#D0D0D0",
    borderWidth: 1,
    borderStyle: "solid",
    alignItems: "center",
    alignSelf: "center",
    justifyContent: "center",
    lineHeight: 48,
    marginTop: 50,
    shadowColor: "#333333",
    shadowOffset: {
      width: 0,
      height: 0.5,
    },
    shadowOpacity: 0.2,
    shadowRadius: 1.41,
    elevation: 2,
  },

  btntext: {
    fontSize: 16,
    fontWeight: "bold",
    color: "#AFAFAF",
    textShadowColor: "rgba(0, 0, 0, 0.1)",
    textShadowOffset: { width: -0.5, height: 0.5 },
    textShadowRadius: 10,
  },
});

export default LogIn;