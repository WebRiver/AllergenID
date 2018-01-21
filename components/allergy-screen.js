import React from 'react';
import { View, ScrollView, Text, Button, StyleSheet} from 'react-native';
import { StackNavigator } from 'react-navigation';
import Expo from 'expo';
import CheckBox from 'react-native-checkbox';

class AllergyScreen extends React.Component {
    static navigationOptions = {
        title: "Select Allergies",
    };
    constructor(props) {
        super(props);
        this.state = {
            cornChecked: false,
            dairyChecked: false,
            glutenChecked: false,
            wheatChecked: false,
            eggsChecked: false,
            fishChecked: false,
            shellfishChecked: false,
            peanutsChecked: false,
            treeNutsChecked: false,
            soyChecked: false,
            $trawberryChecked: false,
    
            Allergens: [],
        };
    }

    

    render() {
        const {navigate} = this.props.navigation;
        return (
            <ScrollView>
                <Text onPress={() => this.setState({cornChecked: (this.state.cornChecked == true) ? false : true})} 
                      style={this.state.cornChecked ? styles.checked : styles.unchecked}>Corn</Text>
                <Text onPress={() => this.setState({dairyChecked: (this.state.dairyChecked == true) ? false : true})} 
                      style={this.state.dairyChecked ? styles.checked : styles.unchecked}>Dairy</Text>
                <Text onPress={() => this.setState({glutenChecked: (this.state.glutenChecked == true) ? false : true})} 
                      style={this.state.glutenChecked ? styles.checked : styles.unchecked}>Gluten</Text>
                <Text onPress={() => this.setState({wheatChecked: (this.state.wheatChecked == true) ? false : true})} 
                      style={this.state.wheatChecked ? styles.checked : styles.unchecked}>Wheat</Text>
                <Text onPress={() => this.setState({eggsChecked: (this.state.eggsChecked == true) ? false : true})} 
                      style={this.state.eggsChecked ? styles.checked : styles.unchecked}>Eggs</Text>
                <Text onPress={() => this.setState({fishChecked: (this.state.fishChecked == true) ? false : true})} 
                      style={this.state.fishChecked ? styles.checked : styles.unchecked}>Fish</Text>
                <Text onPress={() => this.setState({shellfishChecked: (this.state.shellfishChecked == true) ? false : true})} 
                      style={this.state.shellfishChecked ? styles.checked : styles.unchecked}>Shellfish</Text>
                <Text onPress={() => this.setState({peanutsChecked: (this.state.peanutsChecked == true) ? false : true})} 
                      style={this.state.peanutsChecked ? styles.checked : styles.unchecked}>Peanuts</Text>
                <Text onPress={() => this.setState({treeNutsChecked: (this.state.treeNutsChecked == true) ? false : true})} 
                      style={this.state.treeNutsChecked ? styles.checked : styles.unchecked}>Tree Nuts</Text>
                <Text onPress={() => this.setState({soyChecked: (this.state.soyChecked == true) ? false : true})} 
                      style={this.state.soyChecked ? styles.checked : styles.unchecked}>Soy</Text>
                <Text onPress={() => this.setState({$trawberryChecked: (this.state.$trawberryChecked == true) ? false : true})} 
                      style={this.state.$trawberryChecked ? styles.checked : styles.unchecked}>$trawberries</Text>
            </ScrollView>
        );
    }
}

const styles = StyleSheet.create({
    container: {
        flex: 1,
        backgroundColor: '#fff',
        alignItems: 'center',
        justifyContent: 'center',
    },
    unchecked: {
        fontSize: 20,
        padding: 10,
    },
    checked: {
        fontSize: 20,
        padding: 10,
        backgroundColor: 'rgb(179, 216, 253)'
    },
});

export default AllergyScreen;