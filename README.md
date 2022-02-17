# new-react-component

Usage

```
chmod +x path/to/nrc.py

echo "alias nrc='path/to/nrc.py'" >> path/to/my/rc-profile # .zshrc, .bashrc, etc

# later on

nrc path/to/my-awesome-component # MyAwesomeComponent
```

## Results

```typescript
// path/to/index.ts
export { default } from './my-awesome-component';

// path/to/my-awesome-component.tsx
import React, { useState, useEffect } from 'react';
import { Box } from '@drivekyte/web-components';

const MyAwesomeComponent = () => {
	const [loading, setLoading] = useState(false);

	useEffect(() => {
		setLoading(false);
	}, [loading]);

	return (
		<Box>
			<div>MyAwesomeComponent</div>
		</Box>
	);
};

export default MyAwesomeComponent;
```
