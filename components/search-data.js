import React from 'react';
import { View, Text, Button, StyleSheet } from 'react-native';
import { StackNavigator } from 'react-navigation';
import Expo from 'expo';

class SearchData extends React.Component {


    constructor() {
        super();
        this.state = {
            searchText: this.props.navigation.state.params.stext,
            data : []
        }
    }

    getURL() {
        var st = this.searchText;
        var url = "https://api.nal.usda.gov/ndb/search/?format=json&ds=Branded+Food+Products&q=${st}&sort=n&max=10&offset=0&api_key=SW5yC8FS6YfGlesX7P2s7vcM6yKVJ2WEPv0PXjxt";
        return url
    }

    getData() {
        return fetch(getUrl())
            .then((response) => response.json())
            .then((responseJson) => {
                this.setState({data: responseJson.list.item});
            })
            .catch((error) => {
              console.error(error);
            });
    }

    componentDidMount() {
        this.getData();
    }

    render() {
        <SearchDisplay data = {this.state.data} />
    }

}