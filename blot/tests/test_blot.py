from mock import Mock, patch, mock_open

import blot


def make_mocks():
    mocks = Mock()
    mocks.assets = Mock()
    mocks.reader = Mock()
    mocks.reader.read = Mock(return_value=mocks.assets)
    mocks.loader = Mock()
    mocks.processor = Mock()
    mocks.content = Mock()
    mocks.writer = Mock()
    mocks.writer.target = Mock()
    mocks.writer.render = Mock(return_value=[(Mock(), Mock())])
    return mocks


def make_config(mocks):
    return {
        'loader': mocks.loader,
        'reader': mocks.reader,
        'processors': [mocks.processor],
    }


def test_generate_type_context():
    mocks = make_mocks()
    config = make_config(mocks)
    context = blot._generate_type_context(config)
    assert mocks.assets == context["assets"]
    mocks.processor.process.assert_called_with(context)


def test_read():
    mocks = make_mocks()
    config = make_config(mocks)
    context = blot.read({}, {'foo': config})
    assert context == {'foo': {'assets': mocks.assets}}


def test_write():
    mocks = make_mocks()
    context = {}
    writers = [mocks.writer]
    with patch('os.path'):
        with patch('os.path.split', Mock(return_value=(Mock(), Mock()))):
            with patch("__builtin__.open", mock_open):
                blot.write(context, writers)
    mocks.writer.target.assert_called_with({})
    mocks.writer.render.assert_called_with({})


def test_write_no_exists():
    mocks = make_mocks()
    context = {}
    writers = [mocks.writer]
    with patch('os.path'):
        with patch('os.path.split', Mock(return_value=(Mock(), Mock()))):
            with patch("__builtin__.open", mock_open):
                with patch('os.path.exists', Mock(return_value=False)):
                    with patch('os.makedirs'):
                        blot.write(context, writers)
    mocks.writer.target.assert_called_with({})
    mocks.writer.render.assert_called_with({})
