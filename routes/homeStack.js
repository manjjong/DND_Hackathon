import { createStackNavigator } from "react-navigation-stack";
import { createAppContainer } from "react-navigation";
import MainScreen from "../screens/MainScreen";
import LogIn from "../screens/LogIn";
import Challenge from "../screens/Challenge";
import Rank from "../screens/Rank";
import Search from "../screens/Search";
import SignUp from "../screens/SignUp"

const screens = {
  LogIn: {
    screen: LogIn,
  },

  Challenge: {
    screen: Challenge,
  },

  Rank: {
    screen: Rank,
  },

  Search: {
    screen: Search,
  },

  SignUp : {
    screen: SignUp,
  },

  MainScreen: {
    screen: MainScreen,
  },
};

const HomeStack = createStackNavigator(screens);

export default createAppContainer(HomeStack);
