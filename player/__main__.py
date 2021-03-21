from player.app import Player

if __name__ == '__main__':
    player = MusicPlayer()
    player.play(query='사쿠란보')
    player.play(query='조광일 한국')
    print('Finished!')
