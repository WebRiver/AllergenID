import React from 'react';
import { View, Text, Button, StyleSheet, ListView } from 'react-native';
import { StackNavigator } from 'react-navigation';
import Expo from 'expo';

class SearchDisplay extends React.Component {

    render() {
        let search_data = this.props.data.map(function(foods) {
                return {foodName:foods.name,no:foods.nbdno}
            });
            return (
                <View style={styles.container}>
                  <FlatList
                    data={search_data}
                    renderItem={({item}) => <Text style={styles.item}>{item.name}</Text>}
                  />
                </View>
              );
            }
          }
          
    const styles = StyleSheet.create({
    container: {
        flex: 1,
        paddingTop: 22
    },
    item: {
        padding: 10,
        fontSize: 18,
        height: 44,
    },
    })
        