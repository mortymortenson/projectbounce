import bounce_app
import ib
import context
import util

if __name__ == '__main__':
    util.setupLogger('bounce')
    context.init()
    ib.main(bounce_app.BounceApp)
