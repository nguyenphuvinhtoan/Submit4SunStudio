class GameManager {
    private currentState: number[][]
    private magicTubes: number[]

    constructor(initState: number[][], magicTubes: number[]) {
        this.currentState = initState
        this.magicTubes = magicTubes;

        //TODO: init instances of your classes and game logic here

        console.log('INIT GAME:')
        console.log(`Magic tubes indexes: ${magicTubes.join(', ')}`)
        this.printState()
    }

    public move(from: number, to: number): void {
        //TODO: call your methods of your instances to implement move function and update currentState here.

        const tubes = this.currentState.length;
        if(from < 0 || from >= tubes || to < 0 || to >= tubes ) {
            throw new Error("from or to is out of range");
        }
        let chosenFrom = 0;
        // let chosenTo = 0;
        let fromTube = this.currentState[from];
        let toTube = this.currentState[to];
        if(this.magicTubes.includes(from)) {
            if(fromTube[0] === 0) {
                throw new Error("no ball left");
            }  else {
                chosenFrom = fromTube[0];
                let tempTube = [...fromTube];
                for (let index = 0; index < tempTube.length - 1; index++) {
                    tempTube[index] = tempTube[index + 1];
                }
                tempTube[tempTube.length - 1] = 0;
                this.currentState[from] = tempTube;
                this.printState()
            }
        } else {
            let chosenIndex = -1;
            for (let index = fromTube.length - 1; index >= 0; index--) {
                if(fromTube[index] !== 0) {
                    chosenIndex = index;
                    chosenFrom = fromTube[index];
                    fromTube[index] = 0;
                    this.currentState[from] = fromTube;
                    break;
                }
            }
            if(chosenIndex === -1) {
                throw new Error("no ball left");
            }
        }

        if(toTube.every(a => a !== 0)) {
            throw new Error("full of ball");
        } else {
            for (let index = 0; index < toTube.length; index++) {
                if(toTube[index] === 0) {
                    toTube[index] = chosenFrom;
                    this.currentState[to] = toTube;
                    break;
                }

            }
        }


        console.log(`MOVE FROM ${from} TO ${to}:`)
        this.printState()

        if (this.isWin()) {
            console.log("YOU WIN")
        }
    }

    public isWin(): boolean {
        return this.currentState.every(tube => {
            const firstColor = tube[0]
            for (let i = 1; i < tube.length; i++) {
                const color = tube[i]

                if (firstColor != color) return false
            }

            return true
        })
    }

    private printState(): void {
        const transposing = this.currentState[0].map((_, colIndex) => this.currentState.map(row => row[row.length - 1 - colIndex]));

        console.log(transposing.map(row => row.join('\t')).join('\n'))
    }
}

export default GameManager