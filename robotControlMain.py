# coding : utf-8

'''
Copyright 2017-2018 Agnese Salutari.
Licensed under the Apache License, Version 2.0 (the "License"); 
you may not use this file except in compliance with the License. 
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on 
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. 
See the License for the specific language governing permissions and limitations under the License
'''

import time
import RobotWorld

def main():
    DELAY = 0.001 # in seconds
    
    simWorld = RobotWorld.World(host='127.0.0.1', portNumber=19997)
    robBrain = RobotWorld.RobotBrain()
    robBrain.learn('behaviour.pl')
    connectionState = simWorld.connect()
    while connectionState == -1:
        print('Trying to connect to V-REP Simulator...')
        connectionState = simWorld.connect()
    print('Connected to V-REP Simulator.')
    stepCount = 1
    while True:
        print('################## Step: ' + str(stepCount) + ' ##################')
        northPerceptions = []
        for ns in robBrain.getProximitySensorsN():
            data = simWorld.sense(ns)
            northPerceptions.append([ns, data])
        print('State:')
        print(robBrain.getStateN())
        robBrain.thinkN(northPerceptions)
        print('Robot Decision:')
        print(robBrain.getDecision())
        stepCount += 1
        time.sleep(DELAY)

if __name__ == '__main__':
    main()
