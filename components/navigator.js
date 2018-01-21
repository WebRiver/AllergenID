import React from 'react';
import { View, Text, Button, StyleSheet } from 'react-native';
import { StackNavigator } from 'react-navigation';
import SearchBar from './searchbar.js';
import AllergyScreen from './allergy-screen.js';
import HomeScreen from './homescreen.js';
import Expo from 'expo';

const RootNav = StackNavigator(
    {
        Home: {screen: HomeScreen},
        Allergies: {screen: AllergyScreen},
        
    }, 
    {
        navigationOptions: {
            headerStyle: {marginTop: Expo.Constants.statusBarHeight}
        }
    }
);

export default RootNav;