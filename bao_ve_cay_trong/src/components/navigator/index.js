import * as React from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';

import HomeScreen from 'components/home';
import CaptureScreen from 'components/capture';
import PreviewImageScreen from 'components/previewImage';
import Screens from 'until/screens';

const Stack = createStackNavigator();

const Navigator = () => {
	return (
		<NavigationContainer>
			<Stack.Navigator initialRouteName={Screens.HOME} headerMode='none'>
				<Stack.Screen
					name={Screens.HOME}
					component={HomeScreen}
					options={{ title: 'Home Screen' }}
				/>
				<Stack.Screen
					name={Screens.CAPTURE}
					component={CaptureScreen}
				/>
				<Stack.Screen
					name={Screens.PREVIEW}
					component={PreviewImageScreen}
				/>
			</Stack.Navigator>
		</NavigationContainer>
	);
};

export default Navigator;
