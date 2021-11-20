import React, {useState, useEffect }from 'react';
import { TouchableHighlight } from 'react-native';
import { SafeAreaView, View, FlatList, StyleSheet, Text, TouchableOpacity, StatusBar } from 'react-native';

const LIMIT = 11;

const Item = ({ item, onPress, style }) => (
    <TouchableOpacity onPress={onPress} style={[styles.item, style]}>
        <Text style={styles.title}>{item.title}</Text>
    </TouchableOpacity>
);

export default function Chellenge({navigation}) {
  const [data, setData] = useState([]);
  const [offset, setOffset] = useState(0);
  const [loading, setLoading] = useState(false);
  const [selectedId, setSelectedId] = useState(null)

  const getData = () => {
    setLoading(true);
    fetch("http://jsonplaceholder.typicode.com/posts")
      .then((res) => res.json())
      .then((res) => setData(res))
  };

  const renderItem = ({ item }) => {
    //id가 selectedId라면 배경색상 변경
    const backgroundColor = item.id === selectedId ? "#6e3b6e" : "#f9c2ff";

    return (
      <Item
        item={item}
        onPress={() => navigation.navigate('Rank')}
        style={{ backgroundColor }}
      />
    )
  };

  useEffect(() => {
    getData();
  }, []);

  
  return (
    <SafeAreaView style={styles.container}>
        <TouchableHighlight onPress={() => navigation.navigate('MainScreen')}>
            <View style = {styles.btn}>
                <Text style={styles.btntext}>Todo</Text>
            </View>
        </TouchableHighlight>
      <FlatList
        data={data}
        renderItem={renderItem}
        keyExtractor={(item) => String(item.id)}
      />
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
    container: {
      flex: 1,
      backgroundColor: '#fff',
      justifyContent: 'center',
    },
  
    backgroundimage: {
      width: '100%', height: '100%'
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
        marginTop: 10,
        marginRight: 20,
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

      title: {
        fontSize: 32,
      },
});