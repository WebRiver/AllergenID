import React from 'react';
import { View, Text, Button, StyleSheet } from 'react-native';
import { StackNavigator } from 'react-navigation';
import Expo from 'expo';

class SearchDisplay extends React.Component {

    render() {
        let search_data = this.props.data.map(function(foods) {
                return {foodName:foods.name,}
            });
        }
    }