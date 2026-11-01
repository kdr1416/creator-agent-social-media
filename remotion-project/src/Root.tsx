import React from 'react';
import { Composition } from 'remotion';
import { Scene2 } from './Scene2';

export const RemotionRoot: React.FC = () => {
  return (
    <Composition
      id="Scene2"
      component={Scene2}
      durationInFrames={177}
      fps={30}
      width={720}
      height={1280}
    />
  );
};
