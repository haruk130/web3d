
    var blks = []
    function makeworld(x,y,z) { // size x,y,z
        blks = Array.from(Array(y),_=>Array.from(Array(x),_=>Array(z).fill(0)));
        for (i=0;i<200;i++) {
            //blks[Math.floor(Math.random()*y)][Math.floor(Math.random()*x)][Math.floor(Math.random()*(z-1)+1)] = Math.floor(Math.random()*4)+1
        }
        blkd = [
            // [],
            // [[],[0,1,1,1,1],[0,1,1,1,1],[0,1,1,1,1],[0,1,1,1,1],[0,1,1,1,1],[0,1,1,1,1]],
            // [[],[0,1,1,1,0],[0,1,1,1,0],[0,1,1,1,0],[0,1,1,1,0],[0,1,1,1,0],[0,1,1,1,0]],
            // [[],[0,1,1,0,0],[0,1,1,0,0],[0,1,1,0,0],[0,1,1,0,0],[0,1,1,0,0],[0,1,1,0,0]],
            // [[],[0,1,0,0,0],[0,1,0,0,0],[0,1,0,0,0],[0,1,0,0,0],[0,1,0,0,0],[0,1,0,0,0]],
        ]
        for (let ly=0;ly<y;ly++) {
            for (let lx=0;lx<x;lx++) {
                for (let lz=0;lz<z;lz++) {
                    if (blkd[ly]!=null&&blkd[ly][lx]!=null&&blkd[ly][lx][lz]!=null&&blkd[ly][lx][lz]!=0) {
                        blks[ly][lx][lz] = 1
                    }
                }
            }
        }
        for (let ly=0;ly<y;ly++) {
            for (let lx=0;lx<x;lx++) {
                blks[ly][lx][0] = 1
            }
        }
    }
    blkcs = {
        1:[212,210,254],
        2:[212,101,120],
        3:[112,202,120],
        4:[112,120,230],
        5:[212,221,120],
        6:[112,220,230],
        7:[213,100,220],
    }

    function datato3d() {

        

        x = blks[0].length;
        y = blks.length;
        z = blks[0][0].length;
        scene["game"] = [[0],[]];
        fmaze = scene["game"][1];

        let txtname = 400

        for (let ly=0;ly<y;ly++) {
            for (let lx=0;lx<x;lx++) {
                for(let lz=0;lz<z;lz++) {
                    if (blks[ly][lx][lz]!=0) {
                        c = blkcs[blks[ly][lx][lz]];
                        if (txtname==0) {
                            // console.log(blks[ly][lx][lz])
                            // 上面
                            if (!(lx>0&&blks[ly][lx][lz+1]!=0)||blks[ly][lx][lz+1]==null) {
                                fmaze.push([[lx,ly,lz+1],[lx+1,ly,lz+1],[lx+1,ly+1,lz+1],[0],[c[0]],[c[1]],[c[2]],[0],[lx,ly,lz],[0,0,1]])
                                fmaze.push([[lx,ly+1,lz+1],[lx,ly,lz+1],[lx+1,ly+1,lz+1],[0],[c[0]],[c[1]],[c[2]],[0],[lx,ly,lz],[0,0,1]])
                            }
                            // 底面
                            if (!(lx>0&&blks[ly][lx][lz-1]!=0)||blks[ly][lx][lz-1]==null) {
                                fmaze.push([[lx,ly,lz+0],[lx+1,ly+1,lz+0],[lx+1,ly,lz+0],[0],[c[0]],[c[1]],[c[2]],[0],[lx,ly,lz],[0,0,-1]])
                                fmaze.push([[lx,ly+1,lz+0],[lx+1,ly+1,lz+0],[lx,ly,lz+0],[0],[c[0]],[c[1]],[c[2]],[0],[lx,ly,lz],[0,0,-1]])
                            }
                            // 横面
                            if (!(lx>0&&blks[ly][lx-1][lz]!=0)) {
                                fmaze.push([[lx,ly,lz+0],[lx,ly,lz+1],[lx,ly+1,lz+0],[0],[c[0]],[c[1]],[c[2]],[0],[lx,ly,lz],[-1,0,0]]);
                                fmaze.push([[lx,ly,lz+1],[lx,ly+1,lz+1],[lx,ly+1,lz+0],[0],[c[0]],[c[1]],[c[2]],[0],[lx,ly,lz],[-1,0,0]]);
                            }
                            
                            if (!(ly<y-1&&blks[ly+1][lx][lz]!=0)) {
                                fmaze.push([[lx,ly+1,lz+0],[lx,ly+1,lz+1],[lx+1,ly+1,lz+1],[0],[c[0]],[c[1]],[c[2]],[0],[lx,ly,lz],[0,1,0]]);
                                fmaze.push([[lx+1,ly+1,lz+0],[lx,ly+1,lz+0],[lx+1,ly+1,lz+1],[0],[c[0]],[c[1]],[c[2]],[0],[lx,ly,lz],[0,1,0]]);
                            }
                            
                            if (!(lx<x-1&&blks[ly][lx+1][lz]!=0)) {
                                fmaze.push([[lx+1,ly+1,lz+0],[lx+1,ly+1,lz+1],[lx+1,ly,lz+1],[0],[c[0]],[c[1]],[c[2]],[0],[lx,ly,lz],[1,0,0]]);
                                fmaze.push([[lx+1,ly,lz+0],[lx+1,ly+1,lz+0],[lx+1,ly,lz+1],[0],[c[0]],[c[1]],[c[2]],[0],[lx,ly,lz],[1,0,0]]);
                            }
                            
                            if (!(ly>0&&blks[ly-1][lx][lz]!=0)) {
                                fmaze.push([[lx+1,ly,lz+0],[lx+1,ly,lz+1],[lx,ly,lz+1],[0],[c[0]],[c[1]],[c[2]],[0],[lx,ly,lz],[0,-1,0]]);
                                fmaze.push([[lx,ly,lz+0],[lx+1,ly,lz+0],[lx,ly,lz+1],[0],[c[0]],[c[1]],[c[2]],[0],[lx,ly,lz],[0,-1,0]]);
                            }
                        }
                        else {
                            let txtr = field_blocks[txtname]
                            let bs = fieldbs;
                            
                            // 上面
                            if (!(lx>0&&blks[ly][lx][lz+1]!=0)||blks[ly][lx][lz+1]==null) {
                                fmaze.push([[lx,ly,lz+1],[lx+1,ly,lz+1],[lx+1,ly+1,lz+1],[txtname],[0,0],[bs,0],[bs,bs],[0],[lx,ly,lz],[0,0,1]])
                                fmaze.push([[lx,ly+1,lz+1],[lx,ly,lz+1],[lx+1,ly+1,lz+1],[txtname],[0,bs],[0,0],[bs,+bs],[0],[lx,ly,lz],[0,0,1]])
                            }
                            // 底面
                            if (!(lx>0&&blks[ly][lx][lz-1]!=0)||blks[ly][lx][lz-1]==null) {
                                fmaze.push([[lx,ly,lz+0],[lx+1,ly+1,lz+0],[lx+1,ly,lz+0],[txtname],[0,0],[bs,0],[bs,bs],[0],[lx,ly,lz],[0,0,-1]])
                                fmaze.push([[lx,ly+1,lz+0],[lx+1,ly+1,lz+0],[lx,ly,lz+0],[txtname],[0,bs],[0,0],[bs,+bs],[0],[lx,ly,lz],[0,0,-1]])
                            }
                            // 横面
                            if (!(lx>0&&blks[ly][lx-1][lz]!=0)) {
                                fmaze.push([[lx,ly,lz+0],[lx,ly,lz+1],[lx,ly+1,lz+0],[txtname],[0,bs],[0,0],[bs,+bs],[0],[lx,ly,lz],[-1,0,0]]);
                                fmaze.push([[lx,ly,lz+1],[lx,ly+1,lz+1],[lx,ly+1,lz+0],[txtname],[0,0],[bs,0],[bs,bs],[0],[lx,ly,lz],[-1,0,0]]);
                            }
                            
                            if (!(ly<y-1&&blks[ly+1][lx][lz]!=0)) {
                                fmaze.push([[lx,ly+1,lz+0],[lx,ly+1,lz+1],[lx+1,ly+1,lz+1],[txtname],[0,0],[bs,0],[bs,bs],[0],[lx,ly,lz],[0,1,0]]);
                                fmaze.push([[lx+1,ly+1,lz+0],[lx,ly+1,lz+0],[lx+1,ly+1,lz+1],[txtname],[0,bs],[0,0],[bs,+bs],[0],[lx,ly,lz],[0,1,0]]);
                            }
                            
                            if (!(lx<x-1&&blks[ly][lx+1][lz]!=0)) {
                                fmaze.push([[lx+1,ly+1,lz+0],[lx+1,ly+1,lz+1],[lx+1,ly,lz+1],[txtname],[0,0],[bs,0],[bs,bs],[0],[lx,ly,lz],[1,0,0]]);
                                fmaze.push([[lx+1,ly,lz+0],[lx+1,ly+1,lz+0],[lx+1,ly,lz+1],[txtname],[0,bs],[0,0],[bs,+bs],[0],[lx,ly,lz],[1,0,0]]);
                            }
                            
                            if (!(ly>0&&blks[ly-1][lx][lz]!=0)) {
                                fmaze.push([[lx+1,ly,lz+0],[lx+1,ly,lz+1],[lx,ly,lz+1],[txtname],[0,0],[bs,0],[bs,bs],[0],[lx,ly,lz],[0,-1,0]]);
                                fmaze.push([[lx,ly,lz+0],[lx+1,ly,lz+0],[lx,ly,lz+1],[txtname],[0,bs],[0,0],[bs,+bs],[0],[lx,ly,lz],[0,-1,0]]);
                            }
                            
                        }
    
                    }
                }
            }
        }
        // console.log(fmaze)
    }

    function makeflmove() {
        x = blks[0].length;
        y = blks.length;
        z = blks[0][0].length;
        let ret = Array.from(Array(y),_=>Array.from(Array(x),_=>Array(z).fill(1)));
        for (let ly=0;ly<y;ly++) {
            for (let lx=0;lx<x;lx++) {
                for(let lz=0;lz<z;lz++) {
                    if (blks[ly][lx][lz]!=0) {
                        ret[ly][lx][lz] = 0
                    }
                }
            }
        }
        flmove = ret
    }