import React, {useEffect, useState} from "react";
import { TouchableHighlight } from "react-native";
import { ImageBackground, Button, StyleSheet, Text, View, Image } from "react-native";
import axios from 'axios'

class Rank extends React.Component {
    state = {
      image_url : '',
      challenge_name : '',
      first_ID : '김기호',
      first_Rate : '85',
      secound_ID : '김종민',
      secound_Rate : '80',
      third_ID : '김영주',
      third_Rate : '40',
    };

    attend = async () => {

    }

    render() {
        return (
            <View style = {styles.container}>
                  <Image style={styles.avatar} source={{uri: 'https://bootdey.com/img/Content/avatar/avatar6.png'}}/>
                  <TouchableHighlight onPress = {this.attend}>
                    <View style = {styles.btncontainer}>
                      <Text style = {styles.btntext}>참여하기</Text>
                    </View>
                  </TouchableHighlight>
                  <Text style={styles.rank}> {this.state.challenge_name}</Text>
                  <Text style={styles.rank}> 참여율 Top 3 </Text>
                  <Text style={styles.rank}> 1. {this.state.first_ID} {this.state.first_Rate}%</Text>
                  <Text style={styles.rank}> 2. {this.state.secound_ID} {this.state.secound_Rate}%</Text>
                  <Text style={styles.rank}> 3. {this.state.third_ID} {this.state.third_Rate}%</Text>
            </View>
        );
    }
}

const styles = StyleSheet.create({
    container: {
      flex: 1,
      backgroundColor: '#fff',
      alignItems: 'center',
      justifyContent: 'flex-start',
      flexDirection: 'column'
    },

    avatar: {
      width: 130,
      height: 130,
      borderRadius: 63,
      borderWidth: 4,
      borderColor: "white",
      marginBottom:0,
      alignSelf:'center',
      position: 'absolute',
      marginTop:130
    },

    text1: {
      textAlign: 'left',
      fontWeight: 'bold',
      fontSize: 30,
    },

    btncontainer: {
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
      marginTop: 300,
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

    rank: {
      textAlign: 'center',
      fontWeight: 'bold',
      fontSize: 25,
      marginTop: 50
    },

    backgroundimage: {
      width: '100%', height: '100%'
    },
  
});
  
export default Rank;